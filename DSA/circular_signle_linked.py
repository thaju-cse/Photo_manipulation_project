class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        #just change the position of head to new node
        if (self.head !=None):
            new=node(data)
            new.next = self.head
            self.head = new
            cur = self.head
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=self.head
        else:
            #when linked list is empty
            self.head=node(data)
    def  insertatend(self,data):
        if (self.head)!=None:
            #traverse until 2nd last element then insert new node as last node, using curr
            new = node(data)
            curr=self.head
            while (curr.next)!=None:
                curr=curr.next
            curr.next=head
        else:
            #when linked list is empty
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

            while cur.next!=head:
                l.append(curr.data)
                curr=curr.next
            print(" -> ".join(map(str,l)))
o=sll()
List=[6,7,8,5,4,3]
for i in List:
    o.insertatbeg(i)
o.print()
o.print()