# MOVING BOX

# this is a simple program which lets user move a box across terminal using numbers

# a fun project by one and only me, Anirudh, Toofan ka neta 


# importing module
import os

box = [ ]

# VARIABLES - HARD CODED
x = 0
y = 0
x_limit = 10        # maximum value of x
y_limit = 10        # maximum value of y
quiter = 1          # breaks the execution loop of program 
breaker = False     # condition to break the while loop main_loop() fucntion of game 

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
        breaker = True
   
# # # INTERFACE FUNCTIONS

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')    # for windows
    else:
        os.system('clear')  # for macOS and Linux
        
def farewell():
    '''goodbye message to end the program'''
    clear_terminal()
    print()
    print("THANKS FOR PLAYING")
    print()
        
        
def main_loop():
    """This loop displays the cartesian plane at takes commands to move the box"""
    global x, y, breaker
    
    while True:
        
        # adding trailing points give it aim-like look    
        y_trail = y_limit - (y + 1)
        x_trail = x_limit - (x + 1)    
        
        
        # display part
        print(('   '*x + '.\n')*y, sep = '', end = '')
        print('.  '*x, end = '')
        print(box, end = '')
        print('.  '*x_trail)
        
        print(('   '*x + '.\n')*y_trail)
        
        print("position x axis: ", x)
        print("position y axis: ", y)
        
        motion()

        if breaker == True:
            break
            
        # clearing terminal per iteration
        clear_terminal()
    
    # menu displayed after quitting the game    
    print("CONTINUE PLAYING : \t1")
    print("HOME SCREEN : \tany key")
    print()
    choice = input()
    
    if choice == '1':
        clear_terminal()
        
        breaker = False     # it is important to reset breaker or main_loop will break in first iteration
        main_loop()
        
        
    

def home_page():
    '''This is home screen and menu'''
    global quiter, breaker
    
    #title and decorations
    print('+'*(x_limit*3))
    print('='*(x_limit*3))
    print()
    print(' '*x_limit, "MOVING")
    print(' '*x_limit, "BOX")
    print()
    print('+'*(x_limit*3))
    print('='*(x_limit*3))
    print()
    
    # main menu
    print("PLAY : 1")
    print("EXIT : any key")
    print()
    
    # user input and processing
    choice = input()
    if choice == '1':
        clear_terminal()
        breaker = False
        main_loop()
    else:
        farewell()
        quiter = 0
        

# execution of program starts from her               
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        
while quiter:
    print("made by anirudh")    # glitch fixed : terminal wasn't clearing properly       
    clear_terminal()
    home_page()
    