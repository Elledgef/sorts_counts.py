#Author: Faith Elledge
#Githubuser: elledgf
#date: 10/19
#description: A bubble and insertation sort that count the number of compariosons and exchanges made while
# sorting a list

def insertain_sort(a_list):
    for x in range(1,len(a_list)):
        comparisons = 0
        exchanges = 0
        value: a_list[x]
        pos: x - 1
        while pos >=0  and a_list [pos] < value:
            comparisons += 1
            exchanges += 1
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value

def bubble_sort (a_list):
    for x in range(len(a_list)-1):
        comparisons = 0
        exchanges = 0
        for y in range(len(a_list)-1-x):
            if a_list[y] > a_list[y+1]:
                comparisons += 1
                exchanges +=1
                temp = a_list[y]
                a_list[y] = a_list[y+1]
                a_list[y + 1] = temp






