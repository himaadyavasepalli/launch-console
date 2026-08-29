print("Hello, Welcome to my launch console!")
name = input("Wait a second, I didn't get your name. Mind telling me? ")
menu = True
if menu is True:
    print("1: About me")
    print("2: My goals")
    print("3: Exit")
    print("4: A fun fact about me!")
    number = int(input("Choose 1-4"))
    if number ==1:
        print("Hi, my name is Himaadya and I am a sophomore in high-school graduating 2029!")
    elif number==2:
        print("My goals are to improve my coding skills, gain interview skills and eventually get an internship!")
    elif number==3:
        menu = False
        print("Thanks for visiting!")
    else:
        print("A fun fact about me is that I like pink and yellow!")
