def pr(a):
     if a=="(":
         return 0
     elif a=='+' or a=='-':
         return 1
     elif a=='*' or a=='/':
         return 2
     elif a=='^':
         return 3
s=input()
st=[]
for i in s:
    if i.isalnum():
        print(i,end='')
    elif i=='(':
        st.append(i)
    elif i==')':
        a=st.pop()
        while (a!='('):
            print(a,end='')
            a=st.pop()
    else:
        if len(st)==0:
            st.append(i)
        else:
            if pr(i)>pr(st[-1]):
                st.append(i)
            else:
                while (pr(st[-1]) <= pr(i)):
                    print(st.pop(),end='')
                st.append(i)
while (len(st)):
    print(st.pop(),end='')