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
    def deleteatposition(self):
        elements=list(map(int,input().split()))
        pos=int(input())
        for i in elements:
            obj.insertatend(i)
        if pos==1:
            self.head=self.head.next
        else:
            cur=self.head
            while pos-2:
                cur=cur.next
                pos-=1
            cur.next=cur.next.next
        obj.printing()
    def insertatposition(self):
        elements=list(map(int,input().split()))
        element=int(input())
        pos=int(input())
        for i in elements:
            obj.insertatend(i)
        new_node = node(element)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 1
            while current is not None and count < pos - 1:
                current = current.next
                count += 1
            if current is None:
                print("Position out of range")
                return
            new_node.next = current.next
            current.next = new_node
        obj.printing()
    def removeduplicates(self):
        elements=list(map(int,input().split()))
        for i in elements:
            obj.insertatend(i)
        cur=self.head
        duplicates=[]
        nodes=[]
        while cur!=None:
            if (cur.data) in duplicates:
                cur=cur.next
                continue
            nodes.append(cur)
            duplicates.append(cur.data)
            cur=cur.next
        cur=self.head
        for i in nodes[1::]:
            cur.next=i
            cur=i
        try:
            i.next=None
        except:
            pass
        finally:
            obj.printing()
    def printing(self):
        if (self.head)==None:
            print('None')
        elif (self.head.next)==None:
            print(self.head.data)
        else:
            l=[]
            curr=self.head
            while curr!=None:
                l.append(curr.data)
                curr=curr.next
            print(" -> ".join(map(str,l)))
obj=sll()
obj.removeduplicates()
import random
def generate_random_list():
    num=random.randint(50,100)
    out=[]
    for i in range(num):
        i=random.randint(1,10000)
        if i in out:
            continue
        out.append(i)
    # print("Input:\nelements = ")
    # print(" ".join(map(str,out)))
    return (out)
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
    def print_linked_list(self):
        if (self.head.next)==None:
            print(self.head.data)
        else:
            l=[]
            curr=self.head
            while curr!=None:
                l.append(curr.data)
                curr=curr.next
            print("Output: ")
            print(" -> ".join(map(str,l)))
    def reverse_linkedlist(self):
        password=generate_random_list()
        password_copy=""
        print("input: ")
        reversed_password=''
        for i in password:
            password_copy+=str(i)
            obj_sll.insertatend(i)
        print(password_copy)
        cur=self.head
        while cur!=None:
            reversed_password+=str(cur.data)
            cur=cur.next
        self.head=None
        print("Output: ")
        return reversed_password[::-1]
    def sort_linked_list(self):
        self.head=None
        values=generate_random_list()
        print("Input:" )
        for i in values:
            print(i,end=" ")
        print()
        for i in values:
            i=0
            # obj_sll.insertatend(i)
        cur = self.head
        out=[]
        while cur!=None:
            out.append(cur.data)
            cur=cur.next
        out=sorted(out)
        cur=self.head
        cou=0
        while cur!=None:
            cur.data=out[cou]
            cur=cur.next
            cou+=1
        # obj_sll.print_linked_list()
def borrow_number():
    number1=random.randint(1,10000000)
    number2=random.randint(1,10000000)
    print("Input:")
    print("num1 = ",number1)
    print("num2 = ",number2)
    count=0
    if(number1< number2):
        return -1
    else:
        flag=0
        while(number1!=0 and number2!=0):
            temp1=0
            temp2=number2%10
            if(flag):
                temp1=number1%10-1
            else:
                temp1=number1%10
            if(temp1< temp2):
                count+=1
                flag=1
            else:
                flag=0
            number1=number1//10
            number2=number2//10 
        return count
def swapcase(sentence):
    # sentence=input()
    print("Input:\nsentence = ",sentence)
    letters={'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J','k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T','u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z','A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j','K': 'K', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't','U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}
    out=''
    for i in sentence:
        if i.isalpha():
            out+=letters[i]
            continue
        else:
            out+=i
    return out
    # sentences=[0,"The @QuickBrownFox69 jumped over the Lazy Dog's back!","3LuckyPenguins$ waltzed on the Icy Shores of Antarctica.","In a Galaxy far, Far Away, R2-D2 & C-3PO formed an Unlikely Duo.","#BlueMoon2023 will Illuminate the Night Sky with its Enchanting Glow.","Alice123$ and Bob456# Ventured into the Mysterious Cave.","The $1MillionQuest led Adventurers on a Perilous Journey.","Professor Smith's Lab Experiment went Horribly Wrong: BOOM!","Hiking Enthusiasts Explored the Rocky Mountains, reaching Heights of 14,000 Feet!","$StarshipEnterprise Boldly Went where No One had Gone Before.","Mysterious Symbols *&^%* Appeared on the Ancient Artifact."]
def string_count_reducer(s):
    # s=input()
    print("Input:\nsentence = ",s)
    print("Output:")
    i=1
    c=1
    while i<len(s):
        if s[i]==s[i-1]:
            c+=1
        else:
            print(s[i-1],end="")
            print(c,end="")
            c=1
        i+=1
    print(s[i-1],end="")
    print(c)
    # sentences=[0,"aabbbbbccccddddddeeeeffffgggghhhhiiiijjjjkkkklmmmnnnnnooooppppqqqrrrsssttt","zzzzzzxxxxxxwwwwwwvvvvvvuuuuuuttttttssssssrrrrrqqqqqpppppooooooooonnnnmmm","pppppppqqqqqqqrrrrrrrssssssstttttttuuuuuuuvvvvvvvwwwwwwxxxxxxxyyyyyyzzzzz","bbccccdddddeeeeefffffgggghhhhhiiiiiijjjjjkkkkkllllmmmmnnnnoooopppppqqqqq","qqqqqqqrrrrrrrssssssstttttttuuuuuuuvvvvvvvwwwwwwxxxxxxxyyyyyyzzzzzaaaaa","vvvvvvwwwwwwwxxxxxxxxyyyyyyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz","yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy","ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt","kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk","eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"]
def count_words(sentence):
    print("Input:\nsentence = ",sentence)
    sentence = list(map(str,sentence.split()))
    words=0
    word_count={}
    for i in sentence:
        i=i.lower()
        words+=1
        cou=0
        for j in sentence:
            j=j.lower()
            if i in j:
                cou+=1
        if cou>1:
            word_count[i]=cou
    print("Output:")
    print(words)
    return word_count
    # sentences=[0,"In the depths of a forgotten library, dusty tomes whispered forgotten tales, their parchment pages adorned with annotations from generations of scholars who sought the elusive wisdom hidden within the labyrinthine shelves.","Amidst the echoing whispers of ancient forests, a solitary traveler ventured into the heart of the wilderness, guided only by the faint light of a crescent moon that danced upon the forest floor.","In the bustling metropolis, a neon-lit cityscape stretched out like a digital dreamscape, where skyscrapers pierced the night sky, and the cacophony of traffic became a symphony of urban life.","A curious cat, its emerald eyes gleaming with mischief, tiptoed through a garden of fragrant roses, leaving behind a trail of delicate paw prints in the morning dew.","On the rugged coastline, waves crashed relentlessly against jagged cliffs, carving out secret caves that hid tales of maritime adventure and lost treasure.","In the serene meadow, a blanket of wildflowers swayed in the gentle breeze, painting the landscape with hues of lavender, gold, and crimson.","Deep within the pages of an ancient tome, cryptic runes whispered secrets of forgotten civilizations and arcane rituals to the intrepid reader.","Through the telescope's lens, distant galaxies revealed their cosmic ballet, where stars collided and nebulae shimmered like celestial fireworks.""In a bustling market, the aroma of exotic spices mingled with the chatter of merchants, creating a sensory tapestry that transported visitors to far-off lands.","Beneath a canopy of twinkling stars, a campfire crackled and friends gathered, sharing stories that wove the fabric of their shared adventures.","Inside a quaint cafe, the aroma of freshly brewed coffee enveloped patrons as they savored moments of solitude or engaged in lively conversations that spanned the spectrum of human experience."]
def spiral_matrix():
    arr=[]
    print("Input:")
    n=random.randint(1,30)
    m=random.randint(1,30)
    print("m = ",m)
    print("n = ",n)
    print("arr = ")
    for i in range(n):
        arr.append(generate_random_list(m))
    out=[]
    while arr:
        out+=arr.pop(0)
        arr=(list(zip(*arr)))[::-1]
    print("Output:")
    return out
def vowels(sentence):
    # sentence=input()
    print("Input:\nsentence = ",sentence)
    vowels=['a','e','i','o','u']
    sentence=sentence.lower()
    for i in vowels:
        if i in sentence:
            pass
        else:
            break
    else:
        return True
    return False
    # sentences=[0,"In the depths of a forgotten library, dusty tomes whispered forgotten tales, their parchment pages adorned with annotations from generations of scholars who sought the elusive wisdom hidden within the labyrinthine shelves.","Amidst the echoing whispers of ancient forests, a solitary traveler ventured into the heart of the wilderness, guided only by the faint light of a crescent moon that danced upon the forest floor.","In the bustling metropolis, a neon-lit cityscape stretched out like a digital dreamscape, where skyscrapers pierced the night sky, and the cacophony of traffic became a symphony of urban life.","A curious cat, its emerald eyes gleaming with mischief, tiptoed through a garden of fragrant roses, leaving behind a trail of delicate paw prints in the morning dew.","On the rugged coastline, waves crashed relentlessly against jagged cliffs, carving out secret caves that hid tales of maritime adventure and lost treasure.","In the serene meadow, a blanket of wildflowers swayed in the gentle breeze, painting the landscape with hues of lavender, gold, and crimson.","Deep within the pages of an ancient tome, cryptic runes whispered secrets of forgotten civilizations and arcane rituals to the intrepid reader.","Through the telescope's lens, distant galaxies revealed their cosmic ballet, where stars collided and nebulae shimmered like celestial fireworks.""In a bustling market, the aroma of exotic spices mingled with the chatter of merchants, creating a sensory tapestry that transported visitors to far-off lands.","Beneath a canopy of twinkling stars, a campfire crackled and friends gathered, sharing stories that wove the fabric of their shared adventures.","Inside a quaint cafe, the aroma of freshly brewed coffee enveloped patrons as they savored moments of solitude or engaged in lively conversations that spanned the spectrum of human experience."]
def absolute_difference():
    elements=generate_random_list()
    elements=sorted(elements)
    min=100000
    num1=num2=0
    for i in range(len(elements)-1):
        temp=abs(elements[i]-elements[i+1])
        if min>temp:
            min=temp
            num1=elements[i]
            num2=elements[i+1]
    print("Output:")
    print(min)
    return [num1,num2]
def maximum_frequecy(sentence):
    # sentence=input()
    print("Input:\nsentence = ",sentence)
    unique=[]
    sentence=sentence.lower()
    for i in sentence:
        if i.isalpha():
            unique.append(i)
    unique=list(set(unique))
    unique_dict={}
    counted=[]
    for i in unique:
        cou=sentence.count(i)
        counted.append(cou)
        unique_dict[cou]=i
    counted=sorted(counted)
    if counted[-1]==counted[-2]:
        return 0
    return unique_dict[counted[-1]]
    # sentences=[0,"In the depths of a forgotten library, dusty tomes whispered forgotten tales, their parchment pages adorned with annotations from generations of scholars who sought the elusive wisdom hidden within the labyrinthine shelves.","Amidst the echoing whispers of ancient forests, a solitary traveler ventured into the heart of the wilderness, guided only by the faint light of a crescent moon that danced upon the forest floor.","In the bustling metropolis, a neon-lit cityscape stretched out like a digital dreamscape, where skyscrapers pierced the night sky, and the cacophony of traffic became a symphony of urban life.","A curious cat, its emerald eyes gleaming with mischief, tiptoed through a garden of fragrant roses, leaving behind a trail of delicate paw prints in the morning dew.","On the rugged coastline, waves crashed relentlessly against jagged cliffs, carving out secret caves that hid tales of maritime adventure and lost treasure.","In the serene meadow, a blanket of wildflowers swayed in the gentle breeze, painting the landscape with hues of lavender, gold, and crimson.","Deep within the pages of an ancient tome, cryptic runes whispered secrets of forgotten civilizations and arcane rituals to the intrepid reader.","Through the telescope's lens, distant galaxies revealed their cosmic ballet, where stars collided and nebulae shimmered like celestial fireworks.""In a bustling market, the aroma of exotic spices mingled with the chatter of merchants, creating a sensory tapestry that transported visitors to far-off lands.","Beneath a canopy of twinkling stars, a campfire crackled and friends gathered, sharing stories that wove the fabric of their shared adventures.","Inside a quaint cafe, the aroma of freshly brewed coffee enveloped patrons as they savored moments of solitude or engaged in lively conversations that spanned the spectrum of human experience."]
    # sentences=[0,"The @QuickBrownFox69 jumped over the Lazy Dog's back!","3LuckyPenguins$ waltzed on the Icy Shores of Antarctica.","In a Galaxy far, Far Away, R2-D2 & C-3PO formed an Unlikely Duo.","#BlueMoon2023 will Illuminate the Night Sky with its Enchanting Glow.","Alice123$ and Bob456# Ventured into the Mysterious Cave.","The $1MillionQuest led Adventurers on a Perilous Journey.","Professor Smith's Lab Experiment went Horribly Wrong: BOOM!","Hiking Enthusiasts Explored the Rocky Mountains, reaching Heights of 14,000 Feet!","$StarshipEnterprise Boldly Went where No One had Gone Before.","Mysterious Symbols *&^%* Appeared on the Ancient Artifact."]
def count_numbers():
    nums1=generate_random_list()
    nums2=generate_random_list()
    print("Input: \n nums1 = ")
    print(" ".join(map(str,nums1)))
    print("nums2 = ")
    print(" ".join(map(str,nums2)))
    res=[]
    for i in range(len(nums1)):
        count=0
        for j in range(len(nums2)):
            if (nums2[j]<= nums1[i]):
                count+=1
        res.append(count)
    return res
def remove_space(sentence):
    # sentence=input()
    print("Input:\nsentence = ",sentence)
    out=''
    for i in sentence:
        if i==" ":
            continue
        out+=i
    return out
    # sentences=[0,"In the depths of a forgotten library, dusty tomes whispered forgotten tales, their parchment pages adorned with annotations from generations of scholars who sought the elusive wisdom hidden within the labyrinthine shelves.","Amidst the echoing whispers of ancient forests, a solitary traveler ventured into the heart of the wilderness, guided only by the faint light of a crescent moon that danced upon the forest floor.","In the bustling metropolis, a neon-lit cityscape stretched out like a digital dreamscape, where skyscrapers pierced the night sky, and the cacophony of traffic became a symphony of urban life.","A curious cat, its emerald eyes gleaming with mischief, tiptoed through a garden of fragrant roses, leaving behind a trail of delicate paw prints in the morning dew.","On the rugged coastline, waves crashed relentlessly against jagged cliffs, carving out secret caves that hid tales of maritime adventure and lost treasure.","In the serene meadow, a blanket of wildflowers swayed in the gentle breeze, painting the landscape with hues of lavender, gold, and crimson.","Deep within the pages of an ancient tome, cryptic runes whispered secrets of forgotten civilizations and arcane rituals to the intrepid reader.","Through the telescope's lens, distant galaxies revealed their cosmic ballet, where stars collided and nebulae shimmered like celestial fireworks.""In a bustling market, the aroma of exotic spices mingled with the chatter of merchants, creating a sensory tapestry that transported visitors to far-off lands.","Beneath a canopy of twinkling stars, a campfire crackled and friends gathered, sharing stories that wove the fabric of their shared adventures.","Inside a quaint cafe, the aroma of freshly brewed coffee enveloped patrons as they savored moments of solitude or engaged in lively conversations that spanned the spectrum of human experience."]
for i in range(1,11):
    if i<3:
        print("Sample test case",i,":")
    else:
        print("Hidden test case",i-2,":")
    # print("Output :")
    print("Output:\n",remove_space(sentences[i]))
    # print(" ".join(map(str,spiral_matrix())))
    
    