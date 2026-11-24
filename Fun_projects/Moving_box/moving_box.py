# MOVING BOX

# this is a simple program which lets user move a box across terminal using numbers

# a fun project by one and only me, Anirudh, Toofan ka neta 


# importing module
import os

box = [ ]

x = 0
y = 0 

def move_left():
    """This function decreases value of x axis"""
    global x
    x -= 1
    return x

def move_right():
    """This function increases value of x axis"""
    global x
    x += 1
    return x
    
def move_up():
    """This function decreases value of y axis"""
    global y
    y -= 1
    return y
    
def move_down():
    """This function increases value of y axis"""
    global y
    y += 1
    return y
    
    # IMPORTANT NOTE : Height of the box is calculated by empty lines above box
    # so increasing value of y adds more newline characters, decreasing the height of box

def motion():
    """Takes unput from user to move the box, Wandering area is limited to 10x10 block"""
    nav = input("")

    if nav == '2' and x>0:
        move_up()
    elif nav == '8' and x<10:
        move_down()
    elif nav == '4' and y>0:
        move_left()
    elif nav == '6' and y<10:
        move_right()
    
    
for i in range(10):
    motion()

    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
        

    print('.\n'*y, ',  '*x, box)
