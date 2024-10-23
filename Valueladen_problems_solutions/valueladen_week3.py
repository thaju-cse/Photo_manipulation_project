class Solution():
    def longest_substring(self, s):
        len_sub=[]
        prev=""
        cnt=0
        i=0
        while i <len(s):
            j=i
            cnt=0
            while(j<len(s) and (s[j] not in prev)):
                prev=prev+s[j]
                cnt+=1
                j+=1
            prev=""
            i+=1
            len_sub.append(cnt)
        print(len_sub)
        if(len_sub==[]):
            return 0
        return max(len_sub)
    def int_to_roman(self, num):
        dictt={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        num=list(str(num))
        num.reverse()
        for x in range(len(num)):
            num[x]=int(num[x])*(10**x)
        num.reverse()
        stri = ""
        for z in num:
            flag=0
            if z in dictt:
                stri+=dictt[z]
            else:
                y=list(dictt.keys())
                y.reverse()
                for x in range(len(y)):
                    for a in range(x+1,len(y)):
                        if abs(y[x]-y[a])==z:
                            if y[a]<y[x]:
                                stri+=dictt[y[a]]
                                stri+=dictt[y[x]]
                            else:
                                stri+=dictt[y[x]]
                                stri+=dictt[y[a]]
                            flag=1
                if flag==0:
                    x=0
                    y=list(filter(lambda x:x<=z,dictt))
                    y.sort(reverse=True)
                    while(z>0):
                        if y[x]<=z:
                            stri+=dictt[y[x]]
                            z-=y[x]
                        else:
                            x+=1
        return(stri)
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
    def excel_column(self, n):
        if n<27:
            return chr(ord('A')+(n-1)%26)
        ans=""
        while n>0:
            if n%26==0:
                ans+=chr(ord('A')+25)
                n-=1
            else:
                ans+=chr(ord('A')+n%26-1)
            n//=26
        return ans[::-1]
    def print_vertical(self, s: str) -> List[str]:
        split = s.split()
        
        result = []
        
        maxWordLength = max(len(word) for word in split)
        
        for indexInWord in range(maxWordLength):
            partialResult = []
            for word in split:
                if len(word) > indexInWord:
                    partialResult.append(word[indexInWord])
                else:
                    partialResult.append(" ")
            result.append(partialResult)
        
        output = []
        for partialResult in result:
            output.append(''.join(partialResult).rstrip())
            
        return output
sol=Solution()
print(sol.longest_substring())