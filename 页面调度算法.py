
import random

#共有4个内存块，一个内存块存放一个页面，一个页面存放10条指令，共32个页面,指令在页面中顺序存放

class Block(object):
    def __init__(self,numpage=-1,accessed=0):
        self.numpage=numpage        #页号
        self.accessed=accessed      #访问情况，数值表示多久未被访问

size=4      #内存块数目
count=0     #记录指令的序号
n=0         #缺页数目
block=[]  #内存块
zhilin=[]

def initdata(block):
    for i in range(size):
        a=Block(numpage=-1,accessed=0)
        block.append(a)

def findpage(block,curpage):         #查找物理块中是否有该页面
    for i in range(size):
        if block[i].numpage==curpage:
            return i
    return -1

def findExchange(block):            #查找置换的页号
    pos=0
    for i in range(size):
        if block[i].accessed>block[pos].accessed:
            pos=i
    return pos

def display(block):
    for i in range(size):
        if block[i].numpage!=-1:
            print block[i].numpage,
    print
def randomcin(zhilin):          #生成随机指令序列
    flag=0
    count=raw_input()
    count=int(count)
    print ("生成随机指令序列:")
    for i in range(320):
        zhilin.append(count)
        if flag%2==0:
            count=count+1
            count=count%320
        if flag==1:
            count=random.randint(0,count-2)
        if flag==3:
            count=random.randint(count+1,319)
            #count=count+1+random.randint(0,320-count-1)
        flag=flag+1
        flag=flag%4
        print zhilin[i],
        if (i+1)%10==0:
            print

def findspace(block):
    for i in range(size):
        if block[i].numpage==-1:
            return i
    return -1

def pringpage(zhilin):
    for i in range(320):
        print zhilin[i]%10,
        if i%10==0:
            print

def FIFO(block,n):
    curpage=-1
    exchange=-1
    for i in range(320):
        count=zhilin[i]
        curpage=count/10
        exsist=findpage(block,curpage)
        if exsist==-1:
            space=findspace(block)
            if space==-1:
                exchange=findExchange(block)
                block[exchange].numpage=curpage
                display(block)
                n=n+1
                block[exchange].accessed=-1
            else:
                block[space].numpage=curpage
                display(block)
                n=n+1
        else:
            for i in range(size):
                if block[i].numpage != -1:
                    print block[i].numpage,
            print "指令已在内存，页号为",exsist
        for j in range(size):
            block[j].accessed+=1
    print "缺页次数为：",n
    v=n/320.0*100
    print "缺页率为：",v,"%"

def LRU(blcok,n):
    curpage=-1
    exchange=-1
    for i in range(320):
        count=zhilin[i]
        curpage=count/10
        exsist=findpage(block,curpage)
        if exsist==-1:
            space=findspace(block)
            if space==-1:
                exchange=findExchange(block)
                block[exchange].numpage=curpage
                display(block)
                n=n+1
                block[exchange].accessed=-1
            else:
                block[space].numpage=curpage
                display(block)
                n=n+1
        else:
            block[exsist].accessed=-1
            for i in range(size):
                if block[i].numpage != -1:
                    print block[i].numpage,
            print "指令已在内存，页号为", exsist
        for j in range(size):
            block[j].accessed += 1
    print "缺页次数为：", n
    v = n / 320.0 * 100
    print "缺页率为：", v, "%"

def OPT(block,n):
    curpage=-1
    exchange=-1
    for i in range(320):
        count=zhilin[i]
        curpage=count/10
        exsist=findpage(block,curpage)
        if exsist==-1:
            space=findspace(block)
            if space==-1:
                for h in range(size):
                    for k in range(i,320):
                        if block[h].numpage!=zhilin[k]/10:
                            block[h].accessed=1000
                        else:
                            block[h].accessed=k
                            break
                exchange=findExchange(block)
                block[exchange].numpage=curpage
                display(block)
                n=n+1
            else:
                block[space].numpage=curpage
                display(block)
                n=n+1
        else:
            for i in range(size):
                if block[i].numpage != -1:
                    print block[i].numpage,
            print "指令已在内存，页号为", exsist
    print "缺页次数为：", n
    v = n / 320.0 * 100
    print "缺页率为：", v, "%"

print "输入第一条指令号："
randomcin(zhilin)
initdata(block)
while 1:
    print "输入1运行FIFO，输入2运行LRU，输入3运行OPT："
    a=raw_input()
    a=int(a)
    if a==1:
        FIFO(block, n)
    elif a==2:
        LRU(block, n)
    elif a==3:
        OPT(block,n)

