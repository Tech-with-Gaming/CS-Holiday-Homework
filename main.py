#Ayush Bhomia CS Holiday Homework:

def ans1():
    Ans_1 = '''Python is designed to be easy to read and write. The syntax is clear, which makes it accessible for beginners. Unlike compiled languages where the code is translated into machine language before it is run, Python code is executed by an interpreter in real-time.'''
    print('Ans 1:', Ans_1)

def ans2():
    Ans_2 = '''Interactive Mode: In interactive mode, we can type in Python code directly into the Python interpreter and see the results immediately.\n \nScript Mode: Script mode is used for writing larger programs, saving our code for later use, and creating reusable code modules.'''
    print('Ans 2:', Ans_2)

def ans3():
    Ans_3 = '''A cross platform programming language is a programming language that enables developes to develop apps for various platforms using a single codebase, such as Python, Java, C++ etc.'''
    print('Ans 3:', Ans_3)

def ans4():
    Ans_4 = '''Keywords are the predefined and specific reserved words, whereas identifiers is a name given to a variable.'''
    print('Ans 4:', Ans_4)

def ans5():
    Ans_5 = '''Python supports 2 types of Strings. \n \nSingle-Line Strings: Single Line Strings are terminated in single line. Ex: "Hello World"\n \nMulti-Line Strings: Multi-Line Strings store multipe lines of text.'''
    print('Ans 5:', Ans_5)

def ans6():
    Ans_6 = '''Three Factors guide the choice of Indentifiers: \n \n1. An Identifier must start with a letter or an underscore.\n \n2. It should not contain any reserved keyword or any previouly used identifier.\n \n3. It should not contain any special character other than underscore.'''
    print('Ans 6:', Ans_6)

def ans7():
    Ans_7 = '''The error in the following program will be 'Undefined variable' name. A solution to this will be\n \nname = 'Ayush'\nprint ("My name is ", name)'''
    print('Ans 7:', Ans_7)

def ans8():
    Ans_8 = '''C = int(input("Enter the Temperature in Celsius: "))\nF = C*9/5+32\nprint("The temperature in Fahrenheit is:", F)'''
    print('Ans 8:\n\n', Ans_8)

def ans9():
    Ans_9 = '''The Output is: \n2 3 6\n11 3 33'''
    print("Ans 9:", Ans_9)

def ans10():
    Ans_10 = '''radius = float(input("Enter the radius of the circle: "))\narea = 3.14159 * radius ** 2\nprint(f"The Area of the circle is {format(area)}")'''
    print("Ans 10:\n\n",Ans_10)

def ans11():
    Ans_11 = '''height_cm = float(input("Enter your height in centimeters: "))\n\nheight_feet = height_cm / 30.48\nheight_inches = height_feet * 12\nprint(f"Your height is {format(height_feet)} feet and {format(height_inches)} inches."'''
    print("Ans 11:\n\n",Ans_11)

def ans12():
    Ans_12 = '''name = input("Enter your name: ")\nclass_name = input("Enter your class: ")\nage = int(input("Enter your age: "))\n\nprint(f"Name: {name}, Class: {class_name}, Age: {age}")\n\nprint(f"Name: {name}\nClass: {class_name}\nAge: {age}")'''
    print("Note: We will use escape sequence backslash n to make the output come in another line.")
    print("Ans 12:\n\n",Ans_12)


def ans13():
    Ans_13 = '''Data Types are different types of Data stored in a computer. Pythons built in core Data Types are:\n1. Numbers\n2. String\n3. List\n4. Tuple\n5. Dictionary'''
    print("Ans 13:", Ans_13)

def ans14():
    Ans_14 = '''Functions are a bundle/set of programs which can be used repeatedly in the code. In order to repeat the entire program again we can use functions to repeat them which is efficient and time saving.'''
    print("Ans 14:", Ans_14)

def ans15():
    Ans_15 = '''string = input("Enter the String: ")\nfrequency = len(string)\nprint(f"The Frequency of {string} is {frequency})'''
    print("Ans 15:\n", Ans_15)


def ask():
    print("----------Holiday Homework By Ayush Bhomia----------")
    print('\n')
    print("Total Questions: 15")
    print('\n')
    a = input("--> Which Answer Do you want? Make sure to use the format a(answer number), Ex: If you want Answer 1 than type a1 similarly a2. Type [all] if you want all Answers: ")
    if a == "a1":
        print('\n')
        ans1()
        print('\n')
        print("----------Thank You for using the Program----------")
    elif a == "a2":
        print('\n')
        ans2()
        print('\n')
        print("----------Thank You for using the Program----------")
    elif a == "a3":
        print('\n')
        ans3()
        print('\n')
        print("----------Thank You for using the Program----------")
    elif a == "a4":
        print('\n')
        ans4()
        print('\n')
        print("----------Thank You for using the Program----------")
    elif a == "a5":
        print('\n')
        ans5()
        print('\n')
        print("----------Thank You for using the Program----------")
    elif a == "a6":
        print('\n')
        ans6()
        print('\n')
        print("----------Thank You for using the Program----------")
    elif a == "a7":
        print('\n')
        ans7()
        print('\n')
        print("----------Thank You for using the Program----------")
    elif a == "a8":
        print('\n')
        ans8()
        print('\n')
        print("----------Thank You for using the Program----------")
    elif a == "a9":
        print('\n')
        ans9()
        print('\n')
        print("----------Thank You for using the Program----------")
    elif a == "a10":
        print('\n')
        ans10()
        print('\n')
        print("----------Thank You for using the Program----------")
    elif a == "a11":
        print('\n')
        ans11()
        print('\n')
        print("----------Thank You for using the Program----------")
    elif a == "a12":
        print('\n')
        ans12()
        print('\n')
        print("----------Thank You for using the Program----------")
    elif a == "a13":
        print('\n')
        ans13()
        print('\n')
        print("----------Thank You for using the Program----------")
    elif a == "a14":
        print('\n')
        ans14()
        print('\n')
        print("----------Thank You for using the Program----------")
    elif a == "a15":
        print('\n')
        ans15()
        print('\n')
        print("----------Thank You for using the Program----------")
    elif a == "all":
        print('\n\n')
        ans1()
        print('\n\n')
        ans2()
        print('\n\n')
        ans3()
        print('\n\n')
        ans4()
        print('\n\n')
        ans5()
        print('\n\n')
        ans6()
        print('\n\n')
        ans7()
        print('\n\n')
        ans8()
        print('\n\n')
        ans9()
        print('\n\n')
        ans10()
        print('\n\n')
        ans11()
        print('\n\n')
        ans12()
        print('\n\n')
        ans13()
        print('\n\n')
        ans14()
        print('\n\n')
        ans15()
        print('\n')
        print("----------Thank You for using the Program----------")
    else:
        print("Please enter a Valid Argument")
        print('\n')
        print("----------Thank You for using the Program----------")

ask()