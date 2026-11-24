# MOVING BOX

# this is a simple program which lets user move a box across terminal using numbers

# a fun project by one and only me, Anirudh, Toofan ka neta 


# importing module
import os

box = [ ]

# VARIABLES - HARD CODED
x = 0
y = 0
x_limit = 10
y_limit = 10

breaker = True

# # # NAVIGATION FUNCTIONS

def move_left():
    """This function decreases value of x axis"""
    global x
    x -= 1
    
    

def move_right():
    """This function increases value of x axis"""
    global x
    x += 1
    
    
    
def move_up():
    """This function decreases value of y axis"""
    global y
    y -= 1
    
    
    
def move_down():
    """This function increases value of y axis"""
    global y
    y += 1
    
    # IMPORTANT NOTE : Height of the box is calculated by empty lines above box
    # so increasing value of y adds more newline characters, decreasing the height of box



def motion():
    """Takes unput from user to move the box, Wandering area is limited to 10x10 block"""
    global breaker
    
    
    nav = input("")

    if nav == '2' and y > 0:
        move_up()
    elif nav == '8' and y < y_limit - 1:    # -1 because counting is starting from 0
        move_down()
    elif nav == '4' and x > 0:
        move_left()
    elif nav == '6' and x < x_limit - 1:
        move_right()
    elif nav.lower() == 'q':
        breaker = False
   
# # # INTERFACE FUNCTIONS

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')    # for windows
    else:
        os.system('clear')  # for macOS and Linux
        
        
        
while breaker:
    motion()

    # clearing terminal per iteration
    clear_terminal()
    
    # adding trailing parts give it aim-like look    
    y_trail = y_limit - (y + 1)
    x_trail = x_limit - (x + 1)    
    
    print(('   '*x + '.\n')*y, sep = '', end = '')
    print('.  '*x, end = '')
    print(box, end = '')
    print('.  '*x_trail)
    
    print(('   '*x + '.\n')*y_trail)
    
    print("position x axis: ", x)
    print("position y axis: ", y)
