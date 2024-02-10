list1 = list()

#Getting the input of number of elements to be added in the list
inp = int(input("How many elements do you want to add in the list? (Element can be both positive and negative) "))

#Taking the input of elements to be added
for i in range(inp):
    a = int(input("Enter the elements: "))
    list1.append(a)

#Printing the list
print("The list with all the elements: ",list1)

#Defining list2 and list3 to store positive and negative elements of the list
list2 = list()
list3 = list()

#Looping through list to segregate positive and negative numbers
for j in range(inp):
    if list1[j] < 0:
        #Appending negative elements to list3
        list3.append(list1[j])
    else:
        #Appending positive elements to list2
        list2.append(list1[j])

print("The list with positive elements: ",list2)
print("The list with negative elements: ",list3)