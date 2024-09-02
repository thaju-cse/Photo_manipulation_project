def arrays():
    array=[]
    temp=[]
    for i in range(51,101):
        temp.append(i)
        if i%5==0:
            array.append(temp)
            temp=[]


    def search(target,m,n):
        if m==0:
            return False
        left,right=0, m*n-1
        while left<=right:
            mid= left+(right-left)//2
            mid_element=array[mid//n][mid%n]
            if target== mid_element:
                return True
            elif target < mid_element:
                right=mid-1
            else:
                left=mid+1
        return False


    m=len(array)
    n=len(array[0])

    print(search(99,m,n))









    