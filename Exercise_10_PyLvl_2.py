from random import *

#5_1
"""
def unic(item):
    return len(set(item)) == len(item)

list_1 = [randint(1,10) for i in range(randint(5, 10))]
print(f"Unic {list_1} ? = {unic(list_1)}")
"""
#5_2
#def all_first(item_1, item_2):
#    return [el for el in item_1 if not el in item_2]
"""
def all_first(item_1, item_2):
    return list( set(item_1) - set(item_2) )

list_1 = [randint(1,10) for i in range(randint(5, 10))]
list_2 = [randint(1,10) for i in range(randint(5, 10))]

print(f"Elem list_1 {list_1}\n{list_2} \nUnic ele from list_1 {all_first(list_1, list_2)}")
"""
#5_3
"""
def all_first(item_1, item_2):
    return set(item_2) - set(item_1)

list_1 = [randint(1,10) for i in range(randint(5, 10))]
list_2 = [randint(1,10) for i in range(randint(5, 10))]

print(f"Elem list_1 {list_1}\n{list_2} \nUnic ele from list_1 {all_first(list_1, list_2)}")
"""

#6
str_1 = """McCain 10
McCain 3
Obama 19
Obama 2
McCain 7
McCain 2
Obama 6
Obama 10
McCain 11
McCain 5
Obama 3
Obama 12
McCain 13
Aladin 101
Aladin 10"""

#print(str_1)
"""
list_1 = str_1.split()

dict_1 = dict()
print(list_1)

for i in range(0,len(list_1),2):
    if not list_1[i] in list(dict_1.keys()):
        print("Saved")
        dict_1[ list_1[i] ] = int(list_1[i+1])
    else:
        print("Updated")
        dict_1[list_1[i]] += int(list_1[i + 1])

print({ key : dict_1[key] for key in sorted(dict_1.keys()) })
"""

#7
str_1 = """Death there mirth way the noisy merit. Piqued shy spring nor six though mutual living ask extent. Replying of dashwood advanced ladyship smallest disposal or. Attempt offices own improve now see. Called person are around county talked her esteem. Those fully these way nay thing seems.
At distant inhabit amongst by. Appetite welcomed interest the goodness boy not. Estimable education for disposing pronounce her. John size good gay plan sent old roof own. Inquietude saw understood his friendship frequently yet. Nature his marked ham wished.
Marianne or husbands if at stronger ye. Considered is as middletons uncommonly. Promotion perfectly ye consisted so. His chatty dining for effect ladies active. Equally journey wishing not several behaved chapter she two sir. Deficient procuring favourite extensive you two. Yet diminution she impossible understood age.
So if on advanced addition absolute received replying throwing he. Delighted consisted newspaper of unfeeling as neglected so. Tell size come hard mrs and four fond are. Of in commanded earnestly resources it. At quitting in strictly up wandered of relation answered felicity. Side need at in what dear ever upon if. Same down want joy neat ask pain help she. Alone three stuff use law walls fat asked. Near do that he help.
Betrayed cheerful declared end and. Questions we additions is extremely incommode. Next half add call them eat face. Age lived smile six defer bed their few. Had admitting concluded too behaviour him she. Of death to or to being other.
Consulted he eagerness unfeeling deficient existence of. Calling nothing end fertile for venture way boy. Esteem spirit temper too say adieus who direct esteem. It esteems luckily mr or picture placing drawing no. Apartments frequently or motionless on reasonable projecting expression. Way mrs end gave tall walk fact bed.
Offered say visited elderly and. Waited period are played family man formed. He ye body or made on pain part meet. You one delay nor begin our folly abode. By disposed replying mr me unpacked no. As moonlight of my resolving unwilling.
Folly words widow one downs few age every seven. If miss part by fact he park just shew. Discovered had get considered projection who favourable. Necessary up knowledge it tolerably. Unwilling departure education is be dashwoods or an. Use off agreeable law unwilling sir deficient curiosity instantly. Easy mind life fact with see has bore ten. Parish any chatty can elinor direct for former. Up as meant widow equal an share least.
With my them if up many. Lain week nay she them her she. Extremity so attending objection as engrossed gentleman something. Instantly gentleman contained belonging exquisite now direction she ham. West room at sent if year. Numerous indulged distance old law you. Total state as merit court green decay he. Steepest sex bachelor the may delicate its yourself. As he instantly on discovery concluded to. Open draw far pure miss felt say yet few sigh.
Out too the been like hard off. Improve enquire welcome own beloved matters her. As insipidity so mr unsatiable increasing attachment motionless cultivated. Addition mr husbands unpacked occasion he oh. Is unsatiable if projecting boisterous insensible. It recommend be resolving pretended middleton."""
"""
i = 0
while i < len(str_1):
    if  not str_1[i].isalnum() and not str_1[i].isspace():
        str_1 = str_1.replace(str_1[i],"")
        i -= 1
    i += 1
str_1 = str_1.lower()
dict_1 = dict()
list_1 = str_1.split()

for el in list_1:
    dict_1[el] = list_1.count(el)

word = "lengerford"
count = 0
for key, val in dict_1.items():
    if len(word) >= len(key) and val > count:
        word = key
        count = val
print(f"word = {word} and count = {count}")

str_1 = str_1.replace(" " + word + " ", " " + word.upper()+ " ")
print(str_1)
"""
"""
str_1 = str_1.replace(".","").lower()
dict_1 = {key : str_1.split().count(key) for key in str_1.split() }
def next(item):
    return item[1]

word = max( (el for el in dict_1.items() if len(el) == min( len(key) for key in dict_1.keys() )  ), key = next )
print(word)
str_1 = str_1.replace(" " + word[0] + " ", " " + word[0].upper()+ " ")
print(str_1)
"""

#8
str_1 = ""
with open("Input_111.txt", "r", encoding="utf-8") as file:
    str_1 = file.read().lower()


glas = "aeuio"
soglas = "qwrtypsdfghjklzxcvbnm"

countG = 0
countS = 0


for el in str_1:
    if el in glas:
        countG += 1
    elif el in soglas:
        countS += 1

"""
i = 0
str_2 = str_1
while i < len(str_2):
    if str_2[i] in glas:
        countG += str_2.count(str_2[i])
        str_2 = str_2.replace(str_2[i], "")

    elif str_2[i] in  soglas:
        countS += str_2.count(str_2[i])
        str_2 = str_2.replace(str_2[i], "")
#print(countS)
"""

if countS > countG:
    dict_1 = {key: str_1.count(key) for key in str_1 if key in soglas}
    def next(item):
        return item[1]
    word = max((el for el in dict_1.items() ), key=next)
    with open("output.txt" , "w", encoding="utf-8") as file:
        file.write(str(word))

elif countS < countG:
    dict_1 = {key: str_1.count(key) for key in str_1 if key in glas}
    def next(item):
        return item[1]
    dict_1 = {key: val for key, val in sorted(dict_1.items(), key = next, reverse = True) }
    #print(list(dict_1.items())[:3])
    with open("output.txt" , "w", encoding="utf-8") as file:
        file.write(str(list(dict_1.items())[:3]))
