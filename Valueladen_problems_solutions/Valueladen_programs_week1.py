def string_remainder():
    s=input()
    cou=0
    value='0'
    for i in s:
        #finding the alphabets
        if i.isalpha():
            cou+=1
            continue
        #finding hidden numbers
        if i.isdigit():
            value+=i
    if value=='0':
        return -1
    return int(value)%cou
def find_word():
    array = list(map(int,input().split()))
    value = int(input())
    out=""
    di={1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
    di[0]=di[value]
    for i in array:
        out+=di[i%value]
    return out
def single_linkded_list():
    class node:
        def __init__(self,data):
            self.data=data
            self.next=None
    class sll:
        def __init__(self):
            self.head=None
        def insertatbeg(self,data):
            #just change the position of head to new node
            if(self.head !=None):
                new=node(data)
                new.next=self.head
                self.head=new
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
                curr.next=new
            else:
                #when linked list is empty
                self.head=node(data)
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
def repeated_numbers():
    numbers=list(map(int,input().split()))
    value=int(input())
    set_values=set(numbers)
    output=[]
    for i in set_values:
        if numbers.count(i)==value:
            output.append(i)
    return output
def product_vowels_consonants_numbers():
    s=input()
    vowels=0
    consonants=0
    numbers=0
    vowel='aeiouAEIOU'
    for i in s:
        if i.isdigit():
            numbers+=1
            continue
        if i.isalpha():
            if i in vowel:
                vowels+=1
            else:
                consonants+=1
    if not vowels:
        vowels+=1
    if not consonants:
        consonants+=1
    if not numbers:
        numbers+=1
    return vowels*consonants*numbers
def subArraySum():
    arr=list(map(int,input().split()))
    sum=int(input())
    n=len(arr)
    for i in range(n):
        curr_sum = arr[i]
        j = i + 1
        while j <= n:
            if curr_sum == sum:
                return True
            if curr_sum > sum or j == n:
                break
        curr_sum = curr_sum + arr[j]
        j += 1
    return False
def students_max_grade():
    marks=[64, 92, 70, 83, 79, 96, 52]
    A=B=C=D=E=0
    for i in marks:
        print(A,B,C,D,E)
        if i<61:
            E+=1
        elif i<71:
            D+=1
        elif i<81:
            C+=1
        elif i<91:
            B+=1
        else:
            A+=1
    print(A,B,C,D,E)
    return max(A,B,C,D,E)
def rani_candies():
    candies_cost=list(map(int,input().split()))
    pocket_money=int(input())
    pocket_money+=pocket_money//10
    candies=0
    for i in range(len(candies_cost)):
        cost=0
        candies=0
        for j in candies_cost[i::]:
            cost+=j
            candies+=1
            if cost==pocket_money:
                return candies
            elif cost>pocket_money:
                break
    return -1
def reverse_linkedlist():
    class node:
        def __init__(self,data):
            self.data=data
            self.next=None
    class sll:
        def __init__(self):
            self.head=None
        def  insertatend(self,data):
            if (self.head)!=None:
                new = node(data)
                curr=self.head
                while (curr.next)!=None:
                    curr=curr.next
                curr.next=new
            else:
                self.head=node(data)
    obj_sll=sll()
    #before work with reverse function make indentation correct
    def reverse():
        password=input()
        reversed_password=''
        for i in password:
            obj_sll.insertatend(i)
        cur=obj_sll.head
        while cur!=None:
            reversed_password+=str(cur.data)
            cur=cur.next
        return reversed_password[::-1]
def sort_linked_list():
    print("commented due to additional code is necessary.")
    # cur = self.head
    # out=[]
    # while cur!=None:
    #     out.append(cur.data)
    #     cur=cur.next
    # out=out.sort()
    # cur=self.head
    # cou=0
    # while cur!=None:
    #     cur.data=out[cou]
    #     cou+=1
    # return head
def subarray_averages():
    array=list(map(int,input().split()))
    k=int(input())
    out=[]
    for i in range(len(array)-(k-1)):
        temp=0
        for j in range(i,i+k):
            temp+=array[j]
        out.append((temp/k).__round__(2))
    return out
def prime_number():

    n=int(input())
    cou=2
    for i in range(4,n):
        for j in range(2,(i//2)+1):
            if i%j==0:
                break
        else:
            cou+=1
            print(i)
    return cou
#Next comments are used as main.py and created outputs, for future use saving these as comments.
# import random
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class sll:
#     def __init__(self):
#         self.head=None
#     def  insertatend(self,data):
#         if (self.head)!=None:
#             new = node(data)
#             curr=self.head
#             while (curr.next)!=None:
#                 curr=curr.next
#             curr.next=new
#         else:
#             self.head=node(data)
#     def print_linked_list(self):
#         if (self.head.next)==None:
#             print(self.head.data)
#         else:
#             l=[]
#             curr=self.head
#             while curr!=None:
#                 l.append(curr.data)
#                 curr=curr.next
#             print("Output: ")
#             print(" -> ".join(map(str,l)))
#     def reverse_linkedlist(self):
#         password=generate_random_list()
#         password_copy=""
#         print("input: ")
#         reversed_password=''
#         for i in password:
#             password_copy+=str(i)
#             obj_sll.insertatend(i)
#         print(password_copy)
#         cur=self.head
#         while cur!=None:
#             reversed_password+=str(cur.data)
#             cur=cur.next
#         self.head=None
#         print("Output: ")
#         return reversed_password[::-1]
#     def sort_linked_list(self):
#         self.head=None
#         values=generate_random_list()
#         print("Input:" )
#         for i in values:
#             print(i,end=" ")
#         print()
#         for i in values:
#             obj_sll.insertatend(i)
#         cur = self.head
#         out=[]
#         while cur!=None:
#             out.append(cur.data)
#             cur=cur.next
#         out=sorted(out)
#         cur=self.head
#         cou=0
#         while cur!=None:
#             cur.data=out[cou]
#             cur=cur.next
#             cou+=1
#         obj_sll.print_linked_list()
# def repeated_numbers(numbers,value):
#     print("Input:")
#     print("numbers=")
#     for i in numbers:
#         print(i,end=" ")
#     print("\nvalue=",value)
#     set_values=set(numbers)
#     output=[]
#     for i in set_values:
#         if numbers.count(i)==value:
#             output.append(i)
#     return output
# def generate_random_list():
#     num=random.randint(10,100)
#     out=[]
#     for i in range(num):
#         i=random.randint(-100,100)
#         # if i in out:
#         #     continue
#         out.append(i)
#     return (out)
# def product_vowels_consonants_numbers(s):
#     print("Input:\ns='",s)
#     vowels=0
#     consonants=0
#     numbers=0
#     vowel='aeiouAEIOU'
#     for i in s:
#         if i.isdigit():
#             numbers+=1
#             continue
#         if i.isalpha():
#             if i in vowel:
#                 vowels+=1
#             else:
#                 consonants+=1
#     if not vowels:
#         vowels+=1
#     if not consonants:
#         consonants+=1
#     if not numbers:
#         numbers+=1
#     return vowels*consonants*numbers
# def subArraySum():
#     arr=generate_random_list()
#     sum=random.randint(100,1000)
#     print("Input:\narr=")
#     print(" ".join(map(str,arr)))
#     print("sum=",sum)
#     n=len(arr)
#     for i in range(n):
#         curr_sum = arr[i]
#         j = i + 1
#         while j <= n:
#             if curr_sum == sum:
#                 return True
#             if curr_sum > sum or j == n:
#                 break
#             curr_sum = curr_sum + arr[j]
#             j += 1
#     return False
# def students_max_grade():
#     marks=generate_random_list()
#     print("Input:\nmarks = ")
#     print(" ".join(map(str,marks)))
#     A=B=C=D=E=0
#     for i in marks:
#         if i<61:
#             E+=1
#         elif i<71:
#             D+=1
#         elif i<81:
#             C+=1
#         elif i<91:
#             B+=1
#         else:
#             A+=1
#     return max(A,B,C,D,E)
# def rani_candies():
#     candies_cost=generate_random_list()
#     print("Input:")
#     pocket_money=random.randint(120,200)
#     print("candies_cost =")
#     print(" ".join(map(str,candies_cost)))
#     print("pocket_money =",pocket_money)
#     pocket_money+=pocket_money//10
#     candies=0
#     for i in range(len(candies_cost)):
#         cost=0
#         candies=0
#         for j in candies_cost[i::]:
#             cost+=j
#             candies+=1
#             if cost==pocket_money:
#                 return candies
#             elif cost>pocket_money:
#                 break
#     return -1
# def subarray_averages():
#     array=generate_random_list()
#     k=random.randint(1,9)
#     print("Input: \narray = ")
#     print(" ".join(map(str,array)))
#     print("k = ",k)
#     out=[]
#     for i in range(len(array)-(k-1)):
#         temp=0
#         for j in range(i,i+k):
#             temp+=array[j]
#         out.append((temp/k).__round__(2))
#     return out
# def prime_number():
#     n=random.randint(1,10000)
#     print("Input:\nn = ",n)
#     cou=2
#     for i in range(4,n):
#         for j in range(2,(i//2)+1):
#             if i%j==0:
#                 break
#         else:
#             cou+=1
#     return cou
# def sandwitches(): 
#     num=random.randint(10,100) 
#     students=generate_random_list(num)
#     sandwiches=generate_random_list(num)
#     print("input: \nstudents =")
#     print(" ".join(map(str,students)))
#     print("sandwiches = ")
#     print(" ".join(map(str,sandwiches)))
#     for i in sandwiches:
#             if i in students:
#                 students.remove(i)
#             else:
#                 break
#     return len(students)
# def countPairs():
#     nums=generate_random_list()
#     target=random.randint(-10,10)
#     print("Input: \nnums =")
#     print(" ".join(map(str,nums)))
#     print("target =",target)
#     cou=0
#     rou=0
#     for i in nums:
#         for j in nums[rou+1::]:
#             if i+j>=target:
#                 continue
#             cou+=1
#         rou+=1
#     return cou
# def find_word():
#     array = generate_random_list()
#     print("Input: \narray = ")
#     print(" ".join(map(str,array)))
#     value = random.randint(1,26)
#     print("value = ",value)
#     out=""
#     di={1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
#     di[0]=di[value]
#     for i in array:
#         out+=di[i%value]
#     return out
# for i in range(1,11):
#     if i<3:
#         print("Sample test case",i,":")
#     else:
#         print("Hidden test case",i-2,":")
#     print("Output :\n",countPairs())