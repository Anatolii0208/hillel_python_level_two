with open("Input_3.txt", "r") as file:
    list_main = list(file.read().split())
    dict_main = dict()
    for i in range(0,len(list_main),3):
        if list_main[i] in list(dict_main.keys()):
            if list_main[i+1] in list(dict_main[list_main[i]].keys()):
                dict_main[list_main[i]][list_main[i+1]] += int(list_main[i+2])
            else:
                dict_main[list_main[i]][list_main[i+1]] = int(list_main[i+2])
        else:
            #print(list_main[i], list_main[i+1])
            dict_main[list_main[i]]=dict()
            dict_main[list_main[i]][list_main[i+1]] = int(list_main[i+2])
list_1 = sorted(list(dict_main.keys()))
s=''
for i in list_1:
    list_2=sorted(list(dict_main[i].keys()))
    s+=i + ' ('
    for j in list_2:
        s += str(j) + ":" + str(dict_main[i][j]) + ") ("
    s = s[:-1]
    s += "\n"
print(s)