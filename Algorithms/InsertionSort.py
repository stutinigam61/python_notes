def Insertion(lst):

    for i in range(1, len(lst)):
        key = lst[i]

        j = i-1

        while j>=0 and lst[j]> key:
            lst[j+1] = lst[j]
            j-= 1
            lst[j+1]= key

lst = [12, 11, 13, 5, 6]
print("Sorted array:", end=" ")
Insertion(lst)
print(lst)





