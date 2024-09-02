import random
def generate_random_list():
    num=random.randint(30,100)
    out=[]
    for i in range(num):
        i=random.randint(1,20)
        # if i in out:
        #     continue
        out.append(i)
    return (out)
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatend(self,data):
        if (self.head)!=None:
            new = node(data)
            curr=self.head
            while (curr.next)!=None:
                curr=curr.next
            curr.next=new
        else:
            self.head=node(data)
    def deleteatposition(self):
        # n=random.randint(1,200)
        n=1
        elements=generate_random_list(n)
        pos=random.randint(1,n)
        print("Input:\nelements ="," ".join(map(str,elements)))
        print("pos = ",pos)
        for i in elements:
            obj.insertatend(i)
        if pos==1:
            self.head=self.head.next
        else:
            cur=self.head
            while pos-2:
                cur=cur.next
                pos-=1
            cur.next=cur.next.next
        obj.print()
        self.head=None
    def insertatposition(self):
        n=random.randint(1,100)
        elements=generate_random_list(n)
        element=random.randint(1,1000)
        pos=random.randint(1,n)
        print("Input:\nelements ="," ".join(map(str,elements)))
        print("element = ",element)
        print("pos = ",pos)
        new_node=node(element)
        for i in elements:
            obj.insertatend(i)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 1
            while current is not None and count < pos - 1:
                current = current.next
                count += 1
            if current is None:
                print("Position out of range")
                return
            new_node.next = current.next
            current.next = new_node
        obj.print()
        self.head=None
    def removeduplicates(self):
        elements=generate_random_list()
        print("Input:\nelements ="," ".join(map(str,elements)))
        for i in elements:
            obj.insertatend(i)
        cur=self.head
        duplicates=[]
        nodes=[]
        while cur!=None:
            if (cur.data) in duplicates:
                cur=cur.next
                continue
            nodes.append(cur)
            duplicates.append(cur.data)
            cur=cur.next
        cur=self.head
        for i in nodes[1::]:
            cur.next=i
            cur=i
        i.next=None
        obj.print()
        self.head=None
    def print(self):
        print("Output:")
        if (self.head)==None:
            print('None')
        elif (self.head.next)==None:
            print(self.head.data)
        else:
            l=[]
            curr=self.head
            while curr!=None:
                l.append(curr.data)
                curr=curr.next
            print(" -> ".join(map(str,l)))
obj=sll()
for i in range(1,11):
    if i<3:
        print("Sample test case",i,":")
    else:
        print("Hidden test case",i-2,":")
    obj.removeduplicates()