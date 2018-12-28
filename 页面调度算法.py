
import random

#����4���ڴ�飬һ���ڴ����һ��ҳ�棬һ��ҳ����10��ָ���32��ҳ��,ָ����ҳ����˳����

class Block(object):
    def __init__(self,numpage=-1,accessed=0):
        self.numpage=numpage        #ҳ��
        self.accessed=accessed      #�����������ֵ��ʾ���δ������

size=4      #�ڴ����Ŀ
count=0     #��¼ָ������
n=0         #ȱҳ��Ŀ
block=[]  #�ڴ��
zhilin=[]

def initdata(block):
    for i in range(size):
        a=Block(numpage=-1,accessed=0)
        block.append(a)

def findpage(block,curpage):         #������������Ƿ��и�ҳ��
    for i in range(size):
        if block[i].numpage==curpage:
            return i
    return -1

def findExchange(block):            #�����û���ҳ��
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
def randomcin(zhilin):          #�������ָ������
    flag=0
    count=raw_input()
    count=int(count)
    print ("�������ָ������:")
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
            print "ָ�������ڴ棬ҳ��Ϊ",exsist
        for j in range(size):
            block[j].accessed+=1
    print "ȱҳ����Ϊ��",n
    v=n/320.0*100
    print "ȱҳ��Ϊ��",v,"%"

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
            print "ָ�������ڴ棬ҳ��Ϊ", exsist
        for j in range(size):
            block[j].accessed += 1
    print "ȱҳ����Ϊ��", n
    v = n / 320.0 * 100
    print "ȱҳ��Ϊ��", v, "%"

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
            print "ָ�������ڴ棬ҳ��Ϊ", exsist
    print "ȱҳ����Ϊ��", n
    v = n / 320.0 * 100
    print "ȱҳ��Ϊ��", v, "%"

print "�����һ��ָ��ţ�"
randomcin(zhilin)
initdata(block)
while 1:
    print "����1����FIFO������2����LRU������3����OPT��"
    a=raw_input()
    a=int(a)
    if a==1:
        FIFO(block, n)
    elif a==2:
        LRU(block, n)
    elif a==3:
        OPT(block,n)

