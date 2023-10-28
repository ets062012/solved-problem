# Initialize an empty list
my_list = []

# Read in the number of commands
n = int(input())

# Iterate through each command
for i in range(n):
    command = input().split()
    
    # Check the type of command and perform the corresponding operation
    if command[0] == "insert":
        my_list.insert(int(command[1]), int(command[2]))
    elif command[0] == "print":
        print(my_list)
    elif command[0] == "remove":
        my_list.remove(int(command[1]))
    elif command[0] == "append":
        my_list.append(int(command[1]))
    elif command[0] == "sort":
        my_list.sort()
    elif command[0] == "pop":
        my_list.pop()
    elif command[0] == "reverse":
        my_list.reverse()
        
    
