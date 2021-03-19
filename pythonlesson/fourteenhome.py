from Train import *

def info_by_number(number, trains):
    for i in trains:
        if i.number == number:
            i.trrain()
            break

def sort_by_number(trains):
    i = 0
    N = 5
    while i < N - 1:
        m = i
        j = i + 1
        while j < N:
            if trains[j].number < trains[m].number:
                m = j
            j += 1
        trains[i], trains[m] = trains[m], trains[i]
        i += 1
    return trains

def sort_by_name(trains):
    i = 0
    N = 5
    while i < N - 1:
        m = i
        j = i + 1
        while j < N:
            if trains[j].name < trains[m].name:
                m = j
            elif trains[j].name == trains[m].name:
                if trains[j].time < trains[m].time:
                    m = j
            j += 1
        trains[i], trains[m] = trains[m], trains[i]
        i += 1
    return trains

trains = [
    Train("e", 1, 11, 34),
    Train("d", 4, 9, 34),
    Train("c", 3, 10, 34),
    Train("b", 6, 18, 34),
    Train("a", 5, 15, 34)
]

trains = sort_by_number(trains)

info_by_number(5, trains)

trains = sort_by_name(trains)

#print(trains[0].name, trains[1].name, trains[2].name, trains[3].name, trains[4].name)