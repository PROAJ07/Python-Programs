# Create an empty dictionary to store phone book data
phonebook = {}

# Get the number of entries to add to the phone book
n = int(input("Enter the number of entries: "))

# Add each name and phone number to the phone book
for i in range(n):
    name = input("Enter a name: ")
    phone = input("Enter a phone number: ")
    phonebook[name] = phone

# Look up a phone number for a particular name
name = input("Enter a name to look up: ")
if name in phonebook:
    print(f"The phone number for {name} is {phonebook[name]}")
else:
    print(f"{name} not found in phonebook")