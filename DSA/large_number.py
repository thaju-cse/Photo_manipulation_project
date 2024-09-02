def largestNumber(nums):
    lst = []
    for ele in nums:
        lst += [str(ele)]
    n = len(lst)
    for i in range(n):
        for j in range(i+1 , n):
            if str(lst[i]) + str(lst[j]) > str(lst[j]) + str(lst[i]):
                continue
            else:
                lst[i] , lst[j] = lst[j] , lst[i]
    ans = ''.join(lst)
    if int(ans) == 0:
        return "0"
    return ans
nums=list(map(int,input().split()))
print(largestNumber(nums))