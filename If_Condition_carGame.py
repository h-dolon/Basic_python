def while_func(b, c):
    while True:
        a=input().lower()
        if a=='help':
            first_function()
           
        elif a=='start':
            if b:
                second_function()
            else:
                b = third_function()
        elif a=='stop':
            if c:
                print('car already stoped')
            else:
                c=True    
                print('car stoped') 
        elif a=='quit':
            break          
        else:
            print('i don\'t understand....')

def first_function():
    print('start~ to start the car')
    print('stop~ to stop the car')
    print('quit~ to quit the car')

def second_function():
    print('Car is already started')    

def third_function():   
    print('car started... Ready to go')
    return True

com=''
start= False
stop= False
while_func(start, stop)
