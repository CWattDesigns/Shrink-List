listA = []
listB = []
#Prints what the program does
print("This program will take in a list and remove a specified number of elements.")
print("The program will then return a new list containing the remaining elements.")
print("Current Elements to be removed: i > 3\n")

#Asks the user for how big the list will be
n = int(input("Enter the number of elements in the list: "))
#Runs a loop to ask the user to input a number at each index of the list
for i in range(0, n):
    print("Enter element No-{}: ".format(i+1))
    element = int(input())
    listA.append(element)
print("Your list: \n", listA)

#Finds numbers less than 5 in a list and adds them to a new list
for i in listA:
    if i < 4:
        listB.append(i)
    i += 1

print("The new list: \n", listB)
