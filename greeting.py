import datetime

now = datetime.datetime.now()

hour = now.hour

if hour < 12:
    print("Good morning")
elif hour > 11 and hour < 18:
    
    print("Good afternoon")
elif hour > 18 and hour < 19:
    print("Good Evening")
else:
    print("Good Night")
def name_func():
    global name
    name = input("What is your name:  ")
name_func()
if len(name) > 2 or len(name) < 12:
    def gender_func():
        global gender
        gender = input("""
        Are you a 
        male(m)
        female(f)
        do not wish to say(d)
        ?          
        """)
    gender_func()

    if gender == "m" or gender == "M" or gender == "male" or gender == "Male":
        print("Mr ", name)

    elif gender == "f" or gender == "female" or gender == "F" or gender == "Female":
        print("Ms ", name)
        
    elif gender == "d" or gender == "D":
        print("Welcome ",name)
    else:
        print("I did not understand you")
elif name.isdigit():
    print("Pls don't put numbers")
    name_func()
else:
    print("I did not understand you.")
    name_func()