from Alleaten import *
from Meeteaten import *
from Grasseaten import *

#realization of sort by kol food
def sort_by_kg_food(animals, N):
    i = 0
    while i < N - 1:
        m = i
        j = i + 1
        while j < N:
            if animals[j].kg_food > animals[m].kg_food:
                m = j
            elif (animals[j].kg_food == animals[m].kg_food) and (animals[j].name_animal > animals[m].name_animal):
                m=j
            j += 1
        animals[i], animals[m] = animals[m], animals[i]
        i += 1
    return animals

#array of animals
animals = [
    Alleaten(23, "meet", 123, "bob"),
    Grasseaten(23, "grass", 1234,"merri"),
    Meeteaten(21, "meet", 12345, "python"),
    Alleaten(231, "meet", 1233, "cpp"),
    Grasseaten(1, "grass", 12343,"sort")
]

#sort by kol food
animals = sort_by_kg_food(animals, 5)

[print(i.name_animal) for i in animals]

[print(animals[i].indificate) for i in range(len(animals) - 3,len(animals))]



list_2 = []
index = 0
for i in animals:
    list_2.append([])
    list_2[index].append(i.name_animal)
    list_2[index].append(i.indificate)
    list_2[index].append(i.kg_food)
    list_2[index].append(i.type_food)
    index+=1;


from csv import *
with open("path.csv", "w", newline="") as ss:
    writer(ss).writerow(list_2)
    #writerow-in line, writerows-in some lines


with open("path.csv", "r", newline="") as ss:
    #print(reader(ss))
    for el in reader(ss):
        print(el)
