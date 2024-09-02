def count_numbers():
    nums1=list(map(int,input().split()))
    nums2=list(map(int,input().split()))
    res=[]
    for i in range(len(nums1)):
        count=0
        for j in range(len(nums2)):
            if (nums2[j]<= nums1[i]):
                count+=1
        res.append(count)
    return res
print(count_numbers())