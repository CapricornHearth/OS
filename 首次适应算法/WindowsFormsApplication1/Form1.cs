using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public struct Nodes {
            public int name, size, start, end;
            public bool state;
            public Nodes(int start, int end, int size,int name=0,  bool state=true)
            {
                //name为0和state为true表示内存未分配
                this.name = name;   //任务编号
                this.start = start;   
                this.end = end;
                this.size = size;
                this.state = state;
            }
        }
        private List<Nodes> AllocList = new List<Nodes>();        
        public Form1()
        {
            InitializeComponent();
            this.Text = "基于空闲分区链的首次适应算法模拟程序";
        }
        private bool judge(List<Nodes> a,int name)
        {
            bool s = false;
            for (int i = 0; i < a.Count(); i++)
            {
                if (a[i].name == name)
                {
                    MessageBox.Show("该编号任务已分配！");
                    return true;
                }
            }
            return false;
        }
        //分配
        private void alloc(ref List<Nodes> a,int taskId,int taskLength)
        {
            for (int i = 0; i < a.Count(); i++)
            {
                Nodes p = a[i];
                if (p.state == true & p.size > taskLength)
                {
                    Nodes q1 = new Nodes(p.start + taskLength, p.end, p.size-taskLength, 0, true);   //空闲块
                    Nodes q2 = new Nodes(p.start, p.start + taskLength - 1, taskLength, taskId, false); //已分配块
                    a.RemoveAt(i);
                    a.Insert(i, q1);
                    a.Insert(i, q2);
                    return;

                }
                if (p.state == true & p.size == taskLength)
                {
                    p.state = false;
                    a[i] = p;
                    return;
                }
            }
            MessageBox.Show("内存空间不足！");
        }
        //释放并合并空闲分区块
        private void free(ref List<Nodes> a,int taskid)
        {
            int x=0;
            for (int i = 0; i < a.Count(); i++)
            {
                Nodes p=a[i];
                if (p.name == taskid)
                {
                    p.state = true;
                    p.name = 0;
                    a[i] = p;
                    x = i;
                    break;
                }
            }
            //向前合并
            if (x - 1 >=0)
            {
                if(a[x-1].state==true)
                {
                    Nodes q = new Nodes(a[x - 1].start, a[x].end, a[x - 1].size + a[x].size, 0, true);
                    a.RemoveAt(x - 1);
                    a.RemoveAt(x - 1);
                    a.Insert(x - 1, q);
                    x = x - 1;
                }
            }
            //向后合并
            if(x+1<a.Count())
            {
                if (a[x + 1].state == true)
                {
                    Nodes q = new Nodes(a[x].start, a[x + 1].end, a[x].size + a[x + 1].size, 0, true);
                    a.RemoveAt(x );
                    a.RemoveAt(x);
                    a.Insert(x, q);
                }
            }
        }
        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }
        private void label1_Click(object sender, EventArgs e)
        {

        }
        //创建作业
        private void button1_Click(object sender, EventArgs e)
        {
            int name = Convert.ToInt32(textBox1.Text);
            int size = Convert.ToInt32(textBox2.Text);
            if (judge(AllocList, name))
            {
                return;
            }
            dataGridView1.Rows.Clear();
            dataGridView2.Rows.Clear();
            alloc(ref AllocList, name, size);
            for(int i=0;i<AllocList.Count();i++)
            {
                if (AllocList[i].state == false)
                {
                    string name1 = Convert.ToString(AllocList[i].name);
                    string start = Convert.ToString(AllocList[i].start);
                    string end = Convert.ToString(AllocList[i].end);
                    string size1 = Convert.ToString(AllocList[i].size);
                    dataGridView1.Rows.Add(new string[] { name1, start,end, size1 });
                }
                if (AllocList[i].state == true)
                {
                    string start = Convert.ToString(AllocList[i].start);
                    string end = Convert.ToString(AllocList[i].end);
                    string size1 = Convert.ToString(AllocList[i].size);
                    dataGridView2.Rows.Add(new string[] {start, end, size1 });
                }
            }
        }
        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }
        //删除作业
        private void button2_Click(object sender, EventArgs e)
        {
            int namedel = Convert.ToInt32(textBox3.Text);
            dataGridView1.Rows.Clear();
            dataGridView2.Rows.Clear();
            free(ref AllocList, namedel);
            for (int i = 0; i < AllocList.Count(); i++)
            {
                if (AllocList[i].state == false)
                {
                    string name1 = Convert.ToString(AllocList[i].name);
                    string start = Convert.ToString(AllocList[i].start);
                    string end = Convert.ToString(AllocList[i].end);
                    string size1 = Convert.ToString(AllocList[i].size);
                    dataGridView1.Rows.Add(new string[] { name1, start, end, size1 });
                }
                if (AllocList[i].state == true)
                {
                    string start = Convert.ToString(AllocList[i].start);
                    string end = Convert.ToString(AllocList[i].end);
                    string size1 = Convert.ToString(AllocList[i].size);
                    dataGridView2.Rows.Add(new string[] { start, end, size1 });
                }
            }
        }
        //初始化
        private void button3_Click(object sender, EventArgs e)
        {
            int ss = Convert.ToInt32(textBox4.Text);
            Nodes a = new Nodes(0, ss - 1, ss, 0, true);
            AllocList.Add(a);
            dataGridView2.Rows.Add(new string[] { "0", Convert.ToString(ss - 1), Convert.ToString(ss) });
        }
        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
