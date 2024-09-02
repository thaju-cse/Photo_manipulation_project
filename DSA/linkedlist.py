class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        
        if(self.head !=None):
            new=node(data)
            new.next=self.head
            self.head=new
        else:
            self.head=node(data)
    def  insertatend(self,data):
        if (self.head)!=None:
            new = node(data)
            curr=self.head
            while (curr.next)!=None:
                curr=curr.next
            curr.next=new
        else:
            self.head=node(data)
    def delatbeg(self):
        if (self.head)==None:
            print("list is empty!!!")
        else:
            # shift head to 2nd element
            print("deleted element is",self.head.data)
            self.head=self.head.next
    def delatend(self):
        if (self.head)==None:
            #when list is not created
            print('List is empty !!!')
        elif (self.head.next)==None:
            #when list has single element
            self.head=None
        else:
            #traverse until 2nd last element then fix curr.next as None
            curr=self.head
            while curr.next.next!=None:
                curr=curr.next
            print('Deleted element is',curr.next.data)
            curr.next=None

    def print(self):
        if (self.head)==None:
            print("List is empty")
        elif (self.head.next)==None:
            print(self.head.data)
        else:
            l=[]
            curr=self.head
            while curr!=None:
                l.append(curr.data)
                curr=curr.next
            print(" -> ".join(map(str,l)))
    def insertany(self,data,pos):
        cur=self.head
        a=0
        while (a!=pos):
            cur=cur.next
            b=cur
            a+=1
        cur.next=node(data)
        cur.next.next=b.next

li=[6]
#list(map(int,input().split()))
o=sll()
for i in li:
    o.insertatend(i)
#o.delatbeg()
o.print()
o.insertatend(23)
o.print()