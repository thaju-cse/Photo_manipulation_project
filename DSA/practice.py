# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class sll:
#     def __init__(self):
#         self.head=None
#     def create(self,data):
#         if (self.head!=None):
#             new=node(data)
#             new.next=self.head
#             self.head=new
#         else:
#             self.head=node(data)
#     def printing(self):
#         cur=self.head
#         while cur!=None:
#             print(cur.data,end=' -> ')
#             cur=cur.next
#     def insertatend(self,data):
#         curr=self.head
#         while cur.next!=None:
#             tmpcur=cur
#             cur=cur.next
#         new=node(data)
#         new.next=None
#         tmpcur.next=
# li=[3,3,4,4,5,6,6]
# o=sll()
# for i in li:
#     o.create(i)
#
# o.printing()
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlell:
    def __init__(self):
        self.head=None
    def inatbeg(self,data):
        if (self.head)!=None:
            new=node(data)
            new.next=self.head
            self.head=new
        else:
            self.head=node(data)
    def max(self):
        temp=0
        cur=self.head
        while cur!=None:
            if cur.data>temp:
                temp=cur.data
            cur=cur.next
        print("The max value in the list is",temp)
    def print(self):
        curr=self.head
        while curr != None:
            print(curr.data,end=" -> ")
            curr=curr.next
li=[4,5,8,6]
o=singlell()
for i in li:
    o.inatbeg(i)
o.max()'''

a=[1,2,3,4]
b=[4,3,2,1]
print(a==a[::-1])