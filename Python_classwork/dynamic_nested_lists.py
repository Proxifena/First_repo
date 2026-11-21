# Program to understand nested lists 
# this program is dynamic



def newlist():
    '''This function is used to make a new list with length and elements defined by the user. User can also make nested lists'''
    
    a = [] # empty list declared
    
    n = int(input("enter length of new list: ")) # taking length of new list from user
    
    
    for i in range(n):
        
        # displaying available commands
        print("Enter 1 for adding integer: ")
        print("Enter 2 for adding new list: ")
        
        choice = input()                    # choice made by user
        
        
        if choice == '1':
            num = input("enter element: ")

            if num.isnumeric():             # integer inputs will automatically be typecasted
                a.append(int(num))           
            else:
                a.append(num)               # other datatypes will enter as string
                
        elif choice == '2':
            b = newlist()                   # recursion to make infinite number of nested lists
            a.append(b)
        else:
            print("invalid input")
        
    return a                                # function returns the final list
    


print("MAKE NESTED LISTS")                  # header in terminal run
print('='*100, '\n')                        # some decorations

ch = input("Do you want to make a list?\n[y/n]")    # asking user before making a list

if ch.lower() == 'y':
    lst1 = newlist()
    print(lst1)

