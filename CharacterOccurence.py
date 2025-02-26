string = input("Please enter a string: ")
char = input("Please enter your own character:  ")
i = 0
count = 0

while(i < len(string)):

    if(string[i] == char):
        count = count + 1
    i = i + 1

#print("Please enter your own character: ")
print("The total number of times", char, "has occured = ", count)