nums=[1,1,1,1,1,1,1,1,1,1,1,1,1,32,32,33,2,3,2,32,32,3,2,32,3,23,2,3,23,23,1,1,1]
num=nums
for i in num:
    c=nums.count(i)
    if c>1:
        while c-1:
            nums.remove(i)
            c-=1
print(nums)
