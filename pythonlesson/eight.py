from os import mkdir, rmdir, remove, rename, listdir, path

#Homework
with open("Input_1.txt", "r") as file:
    list_1 = list(file.read())

    glass = ['a', 'e', 'i', 'o', 'u','а','у','е','ы','о','э','я','и','ю','ё']
    chert=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z','й','ц','к','н','г','ш','щ','з','х','ф','в','п','р','л','д','ж','ч','с','м','т','б']
    dict_glass = {i.lower() : list_1.count(i.lower())+list_1.count(i.upper()) for i in list_1 if i.lower() in glass}
    dict_so_glass = {i.lower() : list_1.count(i.lower())+list_1.count(i.upper()) for i in list_1 if i.lower()  in chert}
    #print(dict_glass)
    kol_glass=sum(list(dict_glass.values()))
    kol_so_glass = sum(list(dict_so_glass.values()))
    if kol_glass<kol_so_glass:
        with open("output.txt", "w") as file:
            for key,val in dict_so_glass.items():
                if val == max(list(dict_so_glass.values())):
                    file.write(key)
                    break
    else:
        with open("output.txt","w") as file:
            list_d = list(dict_glass.items())
            list_d.sort(key=lambda i: i[1],reverse=True)
            answer=''
            for i in range(3):
                answer+=list_d[i][0]
                answer+=","
            file.write(answer[:-1])