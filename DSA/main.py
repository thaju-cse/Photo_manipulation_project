# # import random
# # import datetime
# # def generate_random_list():
# #     num=random.randint(10,10000)
# #     out=[]
# #     for i in range(num):
# #         i=random.randint(1,1000)
# #         if i in out:
# #             continue
# #         out.append(i)
# #     # print("Input:\nelements = ")
# #     # print(" ".join(map(str,out)))
# #     return (out)
# # def int_to_roman(num):
# #     dictt={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
# #     print("\tInput:\n\tnum = ",num)
# #     num=list(str(num))
# #     num.reverse()
# #     for x in range(len(num)):
# #         num[x]=int(num[x])*(10**x)
# #     num.reverse()
# #     stri = ""
# #     for z in num:
# #         flag=0
# #         if z in dictt:
# #             stri+=dictt[z]
# #         else:
# #             y=list(dictt.keys())
# #             y.reverse()
# #             for x in range(len(y)):
# #                 for a in range(x+1,len(y)):
# #                     if abs(y[x]-y[a])==z:
# #                         if y[a]<y[x]:
# #                             stri+=dictt[y[a]]
# #                             stri+=dictt[y[x]]
# #                         else:
# #                             stri+=dictt[y[x]]
# #                             stri+=dictt[y[a]]
# #                         flag=1
# #             if flag==0:
# #                 x=0
# #                 y=list(filter(lambda x:x<=z,dictt))
# #                 y.sort(reverse=True)
# #                 while(z>0):
# #                     if y[x]<=z:
# #                         stri+=dictt[y[x]]
# #                         z-=y[x]
# #                     else:
# #                         x+=1
# #     return(stri)
# # def longest_substring(s):
# #     print("\tInput:\n\tsentence = ",s)
# #     len_sub=[]
# #     prev=""
# #     cnt=0
# #     i=0
# #     while i <len(s):
# #         j=i
# #         cnt=0
# #         while(j<len(s) and (s[j] not in prev)):
# #             prev=prev+s[j]
# #             cnt+=1
# #             j+=1
# #         prev=""
# #         i+=1
# #         len_sub.append(cnt)
# #     if(len_sub==[]):
# #         return 0
# #     return max(len_sub)
# #     # sentences=[0,"Generating random sentences, each with a minimum of 40 words, may result in quite lengthy responses for each sentence. Here are such sentences:","As the sun dipped below the horizon, painting the sky with hues of orange and pink, I couldn't help but feel a sense of tranquility wash over me. Nature's beauty never fails to amaze and inspire.","In the heart of the bustling city, amidst the towering skyscrapers and constant commotion, I found solace in a quaint little café tucked away on a quiet side street. The aroma of freshly brewed coffee enveloped me, and I savored the moments of serenity.","Lost in the pages of a gripping novel, I journeyed to distant lands, met intriguing characters, and embarked on adventures that transcended the boundaries of reality. The power of literature to transport the mind is truly remarkable.","Beneath the starry night sky, I contemplated the vastness of the universe and marveled at the countless galaxies, each with its own secrets waiting to be uncovered. The cosmos holds mysteries beyond our comprehension.","Walking through the lush, emerald forest, I felt a deep connection to the natural world. The rustling leaves, chirping birds, and gentle breeze whispered ancient stories of life's resilience and interconnectedness.","In the midst of a heated debate, I realized the importance of open-mindedness and respectful discourse. Differences in opinion can lead to enlightenment and growth when approached with empathy.","Standing on the precipice of a towering mountain, I gazed down at the breathtaking valley below. The rugged terrain reminded me of the challenges we face in life and the rewards that come with perseverance.","Amidst the chaos of a bustling marketplace, I observed the diversity of cultures, languages, and traditions that coexist harmoniously. The tapestry of humanity is woven with threads of unique experiences.","While savoring a delectable meal prepared with love and care, I reflected on the culinary traditions that bridge generations and bring people together in celebration of flavors and shared memories.","With each step of a long, winding journey, I uncovered new facets of myself and gained a deeper understanding of the world around me. Life s path is a continuous exploration of self-discovery."]
# # def largestNumber():
# #     nums = generate_random_list()
# #     lst = []
# #     print("\tInput:\n\tnums = ")
# #     print(" ".join(map(str,nums)))
# #     for ele in nums:
# #         lst += [str(ele)]
# #     n = len(lst)
# #     for i in range(n):
# #         for j in range(i+1 , n):
# #             if str(lst[i]) + str(lst[j]) > str(lst[j]) + str(lst[i]):
# #                 continue
# #             else:
# #                 lst[i] , lst[j] = lst[j] , lst[i]
# #     ans = ''.join(lst)
# #     if int(ans) == 0:
# #         return "0"
# #     return ans
# # def excel_column(n):
# #     print("\tInput:\n\tn = ",n)
# #     if n<27:
# #         return chr(ord('A')+(n-1)%26)
# #     ans=""
# #     while n>0:
# #         if n%26==0:
# #             ans+=chr(ord('A')+25)
# #             n-=1
# #         else:
# #             ans+=chr(ord('A')+n%26-1)
# #         n//=26
# #     return ans[::-1]
# # def print_vertical(s):
# #     print("\tInput\n\tsentence = ",s)
# #     split = s.split()
# #     result = []
# #     maxWordLength = max(len(word) for word in split)
# #     for indexInWord in range(maxWordLength):
# #         partialResult = []
# #         for word in split:
# #             if len(word) > indexInWord:
# #                 partialResult.append(word[indexInWord])
# #             else:
# #                 partialResult.append(" ")
# #         result.append(partialResult)
# #     output = []
# #     for partialResult in result:
# #         output.append(''.join(partialResult).rstrip())
# #     return output
# #     # sentences=[0,"THE CLEAR BLUE SKY STRETCHED ENDLESSLY, A CANVAS OF PURE AZURE THAT FILLED THE HORIZON FROM EAST TO WEST. BIRDS SOARED HIGH ABOVE, THEIR GRACEFUL FLIGHT A TESTAMENT TO THE FREEDOM OF THE OPEN AIR.","A GENTLE BREEZE RUSTLED THROUGH THE LEAVES OF THE ANCIENT OAK TREE, CREATING A SOOTHING MELODY THAT WHISPERED SECRETS OF THE FOREST. SUNLIGHT FILTERED THROUGH THE DENSE CANOPY, DAPPLING THE GROUND IN SHIFTING PATTERNS OF LIGHT AND SHADOW.","IN THE SILENCE OF THE NIGHT, THE STARS GLITTERED LIKE DIAMONDS IN THE VAST EXPANSE OF THE COSMOS. THE UNIVERSE'S GRANDEUR WAS ON FULL DISPLAY, A COSMIC SPECTACLE THAT HUMBLED THE SOUL.","THE WAVES OF THE OCEAN LAPPED AGAINST THE SHORE, A RHYTHMIC DANCE THAT HAD CONTINUED FOR MILLENNIA. SEASHELLS SCATTERED ALONG THE SAND HELD TALES OF UNDERWATER ADVENTURES AND DISTANT LANDS.","TIME MOVED INEXORABLY FORWARD, A RELENTLESS MARCH THAT CARRIED BOTH THE PAST AND THE FUTURE WITHIN ITS GRASP. THE PRESENT MOMENT, FLEETING AND PRECIOUS, WAS ALL THAT TRULY EXISTED.","IN THE HEART OF THE CITY, SKYSCRAPERS REACHED FOR THE HEAVENS, THEIR SLEEK FACADES REFLECTING THE HUSTLE AND BUSTLE OF URBAN LIFE. PEOPLE HURRIED ALONG BUSY STREETS, EACH WITH THEIR OWN STORY TO TELL.","THE FOREST FLOOR WAS CARPETED WITH A TAPESTRY OF FALLEN LEAVES, THEIR VIBRANT COLORS A TESTAMENT TO THE CHANGING SEASONS. NATURE'S CYCLES CONTINUED, AN ETERNAL RHYTHM OF GROWTH AND DECAY.","HIGH IN THE MOUNTAINS, THE AIR WAS CRISP AND INVIGORATING, A REMINDER OF THE BEAUTY AND CHALLENGES OF HIGH-ALTITUDE LIVING. SNOW-CAPPED PEAKS STOOD AS SENTINELS, GUARDING THE SECRETS OF THE ALPINE WORLD.","DESERT SANDS STRETCHED OUT IN ALL DIRECTIONS, AN ENDLESS SEA OF GOLDEN GRAINS THAT SHIMMERED IN THE RELENTLESS SUN. AMID THE ARID LANDSCAPE, LIFE FOUND A WAY TO THRIVE, RESILIENT AND TENACIOUS.","THE MEANDERING RIVER CARVED A PATH THROUGH THE VALLEY, ITS WATERS A SOURCE OF LIFE AND SUSTENANCE FOR THE COMMUNITIES ALONG ITS BANKS. NATURE'S GIFT OF FLOWING WATER WAS A LIFELINE FOR ALL WHO DEPENDED ON IT."]
# # def generate_random_time():
# #     res=[]
# #     for i in range(random.randint(2,100)):
# #         time=str(datetime.time(hour=random.randint(0,23),minute=random.randint(0,59)))
# #         res.append(time[:-3])
# #     print("\tInput:\n\ttime_stamps = ",res[1:-1])
# #     return res[1:-1]
# # def time_difference(timePoints):
# # 	def convert(time):
# # 		hh, mm = time.split(':')
# # 		return int(hh) * 60 + int(mm)
# # 	time_slots = [False] * 1440
# # 	start, end = 1440, -1
# # 	for time in timePoints:
# # 		minutes = convert(time)
# # 		if time_slots[minutes]:
# # 			return 0
# # 		time_slots[minutes] = True
# # 		start = min(start, minutes)
# # 		end = max(end, minutes)
# # 	prev, res = start, start - end + 1440
# # 	for curr in range(start + 1, end + 1):
# # 		if not time_slots[curr]:
# # 			continue
# # 		res = min(res, curr - prev)
# # 		prev = curr
# # 	return res
# # for i in range(1,11):
# #     if i<3:
# #         print("-> Sample test case",i,":")
# #     else:
# #         print("-> Hidden test case",i-2,":")
# #     print("\tOutput:\n\t",time_difference(generate_random_time()))
    
# import tkinter as tk

# def click(event):
#     text = event.widget.cget("text")
    
#     if text == "=":
#         try:
#             result = str(eval(screen.get()))
#             screen.set(result)
#         except Exception as e:
#             screen.set("Error")
#     elif text == "C":
#         screen.set("")
#     else:
#         screen.set(screen.get() + text)

# root = tk.Tk()
# root.title("Calculator")
# root.geometry("350x450")  
# root.configure(bg="#332d2d")  

# screen = tk.StringVar()

# entry = tk.Entry(root, textvar=screen, font="gray")
# entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

# frame = tk.Frame(root, bg="white")  
# frame.pack()

# buttons = [
#     '7', '8', '9', '+',
#     '4', '5', '6', '-',
#     '1', '2', '3', '*',
#     'C', '0', '=', '/'
# ]

# row, col = 1, 0

# for button in buttons:
#     btn = tk.Button(frame, text=button, padx=20, pady=20, font="white", bg="blue", fg="white")
#     btn.grid(row=row, column=col, padx=5, pady=5)  
#     btn.bind("<Button-1>",click)
#     col += 1
#     if col > 3:
#         col = 0
#         row += 1

# root.mainloop()
# def mys(m):
#     if m == 1:
#         return(1)
#     else:
#         return(m*mys(m-1))
# print(mys(0))
def is_hillvalley(lst):
    if len(lst) < 3:
        return False

    asc_flag = None
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            return False

        if lst[i] > lst[i-1]:
            if asc_flag is False:
                return False
            asc_flag = True
        else:
            if asc_flag is True:
                return False
            asc_flag = False

    return True

def hillvalley(l):
    if len(l) < 4:  # A hill or valley must have at least 4 elements (2 ascending + 2 descending or vice versa)
        return False

    # Check if the list starts with an ascending sequence
    if l[0] < l[1]:
        is_ascending = True
    else:
        is_ascending = False

    # Iterate through the list to find the change in direction
    for i in range(1, len(l)):
        if is_ascending:
            # Check if the sequence changes to descending
            if l[i] >= l[i-1]:
                continue
            else:
                # Check if the remaining elements are in descending order
                if all(l[j] <= l[j+1] for j in range(i, len(l)-1)):
                    return True
                else:
                    return False
        else:
            # Check if the sequence changes to ascending
            if l[i] <= l[i-1]:
                continue
            else:
                # Check if the remaining elements are in ascending order
                if all(l[j] >= l[j+1] for j in range(i, len(l)-1)):
                    return True
                else:
                    return False

    return False

def repfree(s):
  for i in s:
    if s.count(i)>1:
      return False
  return True
# Test cases
test_cases = ["[][]",'!@#$%^&*()']

def transpose(m):
  rows=len(m)
  columns=len(m[0])
  result=[]
  for i in range(columns):
      result.append([0]*rows)
  a=-1
  for i in m:
    a+=1
    b=-1
    for j in i:
      b+=1
      result[b][a]=j
  return result

def mystery(l,v):
  if len(l) == 0:
    return (v)
  else:
    return (mystery(l[:-1],l[-1]+v))


triples = [ (x,y,z) for x in range(2,4) for y in range(2,5) for z in range(5,7) if 2*x*y > 3*z ]


runs = {"Test":{"Rahul":[90,14,35],"Kohli":[3,103,73,42],"Pujara":[53,15,133,8]},"ODI":{"Sharma":[37,99],"Kohli":[63,47]}}

#runs["ODI"]["Rahul"].append([74])
#runs["ODI"]["Rahul"].extend([74])
#runs["ODI"]["Rahul"][0]=74
runs["ODI"]["Rahul"]=[74]
inventory={}
inventory["Amul"] = ["Mystic Mocha",55]
inventory["Amul, Mystic Mocha"] = 55
#inventory[["Amul","Mystic Mocha"]] = 55
inventory[("Amul","Mystic Mocha")] = 55




def orangecap(d):
  players=d.items()
  result={}
  for i in players:
    for j in i[1].items():
      try:
        result[j[0]]+=j[1]
      except:
        result[j[0]]=j[1]
  temp=['',0]
  result=result.items()
  for i in result:
    if i[1]>temp[1]:
      temp=i
  return temp


def multpoly(p1,p2):
  result={}
  for i in p2:
    temp=0
    for j in p1:
      try:        
        result[p1[temp][1]+i[1]]+=p1[temp][0]*i[0]
      except:
        result[p1[temp][1]+i[1]]=p1[temp][0]*i[0]
      temp+=1
  result=result.items()
  final=[]
  print(result)
  for i in result:
    if i[1] == 0:
       continue
    else:
      final.append(i[::-1])
  return final

def addpoly(p1,p2):
  result={}
  for i in p2:
    result[i[1]]=i[0]
  for i in p1:
    try:
      result[i[1]]+=i[0]
    except:
      result[i[1]]=i[0]
  result=result.items()
  final=[]
  for i in result:
    if i[1] == 0:
       continue
    else:
      final.append(i[::-1])
  return final



print(addpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)]))