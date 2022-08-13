#User input
#name = input("what is your name? ")
#print(name)
#age = input("How old are you? ")
#print(age)
#height = input("How tall are you? ")
#print(height)
#question = input("Are you gay(Yes/No)? ")
#print(question + ": really")
#input("? ")
#print('Then You My Proceed')
#---------------------------------------------------------------------------------------------------------------
#Variables
#first_name = "Joshrick"
#last_name = "Abellera"
#full_name = first_name + last_name
#print(full_name)
#---------------------------------------------------------------------------------------------------------------
#String methods
#age = 17
#print("Your age is :" + str(age))
#x = 1 #int
#y = 2 #float
#z = "3" #str
#x = (x)
#y = float(y)
#z = int(z)
#print("X is "+str(x))
#print("Y is GAY THat is Why Y Is equal too " +str(y))
#print(z*
#---------------------------------------------------------------------------------------------------------------
#Type CAsting
#name = "josh"
#print(len(name))
#print(name.find("o"))
#print(name.capitalize())
#print(name.isalpha())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.count("o"))
#print(name.replace("o","t"))
#print(name*9)
#---------------------------------------------------------------------------------------------------------------
#Multiple assignment
#name = "Josh"(longest)
#age = 16
#attractive = True
#print(name)
#print(age)
#print(attractive)
#name, age, attractive, = "Josh", 16, True(Intermidiate)
#print(name)
#print(age)
#print(attractive)
#print (name, age, attractive,)(Quicks)
#---------------------------------------------------------------------------------------------------------------
#Math function
#import math

#pi = 4.30
#Gay = 1
#Lesbian = 2
#Binary = 3
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(math.sqrt(pi))
#print(abs(pi))
#print(pow(pi,5))
#print(max(Gay, Lesbian, Binary))
#print(min(Gay, Lesbian, Binary))
#---------------------------------------------------------------------------------------------------------------
#String slicing
#Slicing = create a subtring by extracting elements  from another slicing
#                      indexing[] or slice()
#                   [start:stop:step]

#name = "Josh Rick"
#first_name = name [:4]
#print(first_name)
#last_name = name [5:10]
#print(last_name)
#choosen_one = name [0:0:2]
#print(choosen_one)
#reversed_name = name [::-1]
#print(reversed_name)

#part 2
#website = "http://google.com"
#website2 = "http://facebook.com"
#website3 = "http://discord.com"
#slice = slice (7,-4)
#print(website3[slice])
#---------------------------------------------------------------------------------------------------------------
 #if statement = a block of code that will execute if it's condition is true

#age = int(input("How old are you?: "))
#if age == 100:
#    print("Then You Are Indeed Gay Just Kiding :You Are A Century Year old")
#elif age >= 18:
#    print("You Are An Adult!")
#elif age < 0:
#    print("You Haven't Not Born Yet")
#else:
#    print("You Are A Child?"
#          " Is this true?")
#chix  =  input("? ")
#print(chix + ": Then You get no bitches")
#---------------------------------------------------------------------------------------------------------------
#While loop = a statemenr that will execute it's block of code
#                 as long as it's condition remains true
#name =""

#while len(name) == 0:
#    name = input("Enter Your name: ")
#print("Hello "+name)
#---------------------------------------------------------------------------------------------------------------
# 2d list
#Mammals = ["Dogs","Cats","Rats"]
#Birds = ["Maya","Agila","Dodo"]
#Fish = ["Tilapya","Gold Fish","Fufu"]
#list = [Mammals,Birds,Fish]
#print(list[2][2])
#---------------------------------------------------------------------------------------------------------------
#for i in range(10,15 +1 ,2):
#    print(i)
#for i in "Josh rick" :
#    print(i)
#For loop
#import time



#for i in range(10,0,-1):
#    print(i)
#    time.sleep(1)
#print("Happy Birthday")

#Tuples
#Student = ("Joshrick","Joshrick",21,"male")

#print(Student.count("Joshrick"))
#print(Student.index(21))
#for x in Student :
#    print(x)

#if "Joshrick" in Student:
#    print("JOshrick Is Here")
#---------------------------------------------------------------------------------------------------------------
#Set{} The is no Duplicate Value
#utensils = {"Fork","Spoon","Knife"}
#dishes = {"Bowl","Plate","Cup","Knife"}
#utensils.add("napkin")
#utensils.remove("Fork")
#utensils.clear()
#utensils.update(dishes)
#dinner_table = utensils.union(dishes)
#print(utensils.difference(dishes))
#print(utensils.intersection(dishes))
#for x in utensils:
#    print(x)
#---------------------------------------------------------------------------------------------------------------
#Poop
#class Car:

#    wheel = (4)

#    def __init__(self,make,model,year,color):
#        self.make = make
#        self.model = model
#        self.year = year
#        self.color = color

#    def drive(self):
#        print("This Car Is Driving")
#
#    def stop(self):
#        print("This "+self.make+" Is Stop")
#
#    def caution(self):
#        print("This "+self.make+" Is Caution")
#---------------------------------------------------------------------------------------------------------------
# Enheritants
#class Animal:

    #alive = True

    #def eat(self):
   #     print("This Animal Can Eat")

  #  def sleep(self):
 #       print("This Animal Can Eat")

#class Rabbit(Animal):
#    def prey(self):
#        print("This Is A Prey")
#---------------------------------------------------------------------------------------------------------------
#Multiple Enheritants part 2
#class Hank(Animal):
 #   def predetor(self):
 #       print("This is a predetor")

#rabbit = Rabbit()
#hank = Hank()

#print(rabbit.alive)
#rabbit.prey()
#hank.eat()
#rabbit.sleep()
#hank.predetor()

#class Organism:

#    alive = True

#class Animal(Organism):

#    def sleep(self):
#        print("This Animal Can Sleep")

#class Rabbit(Animal):

#    def jump(self):
#        print("This Rabbit Can Jump")
#rabbit = Rabbit()

#rabbit.jump()
#print(rabbit.jump)
#---------------------------------------------------------------------------------------------------------------
#Multiple Enheritants part 2
#class Prey:

  #  def prey(self):
 #       print("This Is A Prey")

#class Predetor:

  #  def predetor(self):
 #       print("This Is A Predetor")

#class Rabbit(Prey):
#    pass

#class Shark(Predetor):
#   pass

#class Fish(Predetor,Prey):
 #   pass

#rabbit = Rabbit()
#shark = Shark()
#fish = Fish()
#fish.prey()
#---------------------------------------------------------------------------------------------------------------
#Over Riding
#class Animal:

#    def eat(self):
#        print("This Animal Is Eating")

#class Rabbit(Animal):

#    def eat(self):
#        print("This Rabbit Is Eating")

#animal = Animal()
#rabbit = Rabbit()
#animal.eat()
#rabbit.eat()
#---------------------------------------------------------------------------------------------------------------
#Method Chaining

#class Car:

    #def turn_on(self):
   #     print("This Car Is Turn on")
  #      return self

 #   def drive(self):
#        print("This Car Is Driving")
#        return self

#    def stop(self):
#        print("This Car Is Stopping")
#        return self

#    def turn_off(self):
#        print("This Car Is turn off")
#        return self

#car = Car()
#car.turn_on().drive().stop().turn_on()

#car.turn_on()\
#    .drive()\
#    .stop()\
#    .turn_on()
#---------------------------------------------------------------------------------------------------------------
#super function

#class Rectangle:
#    pass

#class Square(Rectangle):

#    def __int__(self,length,width):
#        self.length
#        self.width

#    def area(self):
#        return self.length * self.width

#class Cube(Rectangle):

#    def __int__(self,length,width):
 #       self.length
 #       self.width
 #       self.height

 #   def volume(self):
#        return self.length * self.width * self.height

#square = Square(3, 3)
#cube = Cube(3, 3, 3)

#Usage Of The Super Function Below

#class Rectangle:
#    def __int__(self, length, width):
#        self.length = length
#        self.width = width


#class Square(Rectangle):

#    def __int__(self, length, width):
#        super().__int__(length, width)

#    def area(self):
#        return self.length*self.width


#class Cube(Rectangle):

#    def __int__(self, length, width):
#        super().__int__(length, width)
#        self.height = height

#    def volume(self):
#        return self.length*self.width*self.height


#square = Square(3,3)
#cube = Cube(3,3,3)

#print(square.area())
#print(cube.volume())

# I Cant Quite Find The Problem With This Code But It Is A TypeError:
# For Now I Need TO Kepp Moving Forward

#---------------------------------------------------------------------------------------------------------------
#ABC Or Abstract Method: It's Like A Ghost
#from abc import ABC, abstractmethod

#class Vehicle(ABC):

#    @abstractmethod
#    def go(self):
#        pass

#    @abstractmethod
#    def stop(self):
#        pass

#class Car(Vehicle):

#    def go(self):
#        print("This Car IS Moving")

#    def stop(self):
#        print("This Car Has Stop")

#class Motorcycle(Vehicle):

#    def go(self):
#        print("This Motorcyle Is Moving")

#    def stop(self):
#        print("This Motorcyle Has Stop")

#car = Car()
#motorcyle = Motorcycle()

#car.go()
#motorcyle.stop()
#---------------------------------------------------------------------------------------------------------------
#Object as argument

#class Car:

#    color = None

#class Motorcycle:

#    color = None

#def change_color(vehicle, color):
 #   vehicle.color = color

#car_1 = Car()
#car_2 = Car()
#car_3 = Car()
#bike_1 = Motorcycle()

#change_color(car_1, "red")
#change_color(car_2,"black")
#change_color(car_3, "white")
#change_color(bike_1, "orange")
#print(car_1.color)
#print(car_2.color)
#print(car_3.color)
#print(bike_1.color)

#---------------------------------------------------------------------------------------------------------------
#Duck Typing:
#If it quack like a duck it walks like a duck then it must be a duck
#when the class the object is important than the method
#class type is not check when methon/attributes are at minimum

#class Duck:

#    def walk(self):
#        print("This Duck Is Walking")

#    def talk(self):
#        print("This Duck Can Quacking")

#class Chicken:

#    def walk(self):
#        print("This Chicken Is Walking")

#    def talk(self):
#        print("This Chicken Can Talk")

#class Person:

#    def catch(self, duck):
#        duck.walk()
#        duck.talk()
#        print("You Catch The Critter")

#duck = Duck()
#chicken = Chicken()
#person = Person()

#person.catch(chicken)
#---------------------------------------------------------------------------------------------------------------
#Walrus operator :=

#happy = False
#print(happy)

#print(happy:=False)

#foods = list()
#while True:
#    food = input("What food do you like : ")
#    if food == "quit" :
#        break
#    foods.append(food)
#foods = list()
#while food := input("What food do you like : ") != "quit":
#    foods.append(food)

#---------------------------------------------------------------------------------------------------------------
# Assigning Function In Variables

#shoot = print
#shoot("Pajdflads")
#i = input
#i("love you")
#def hello():
#    print("HElLO")

#print(hello)
#hi = hello
#print(hi)
#hi()
#hello()
#---------------------------------------------------------------------------------------------------------------
#High Order Function = a function that either
                      #1 accept function as an argument or
                      #return a function
#1                      #(In Python, function are also treated as objects)
#def quite(text):
#    return text.lower()

#def loud(text):
#    return text.upper()

#def hello(func):
#    text = func("Hello")
#    print(text)

#hello(quite)
#hello(loud)
#2
#def divisor(x):
#    def dividend(y):
#        return y / x
#    return dividend

#divide = divisor(2)
#print(divide(10))
#---------------------------------------------------------------------------------------------------------------
# Lumbda function = function written in 1 line using lumbda keyword
#                   accept any number as an arguments, but only has one expression
#                   (think of it as a shortcuy)
#                   (useful if needed in a short period of time, throw-away)
# Lambda Parameter:Expression

#def times(x):
#    return x / 2
#t = times(5)
#print(t)

#def times(x):
#    return x / 2
#print(times(5))

#Using Lambda
#times = lambda x : x * 2

#multiply = lambda x, y : x * y

#add = lambda x, y, z :x+y+z

#full_name = lambda first_name, last_name : first_name+" "+last_name

#age = lambda age : True if age  >= 18 else False
#print(age(17))
#---------------------------------------------------------------------------------------------------------------
# sort() method = used with lists
# sort() function = used list iterables
# Lvl 1
#student = ("Sandy", "Spongebob", "Patrick", "Squidward", "Mr.Krabs")
#student.sort(reverse=True)
#tuple_to_list = sorted(student,reverse=True)
#for i in tuple_to_list:
#    print(i)
# Lvl 2

#student = (("Squidward", "F", 60),
#           ("Sandy", "A", 33),
#           ("Patrick", "D", 12),
#           ("Spongebob", "A", 96))
#grade = lambda grades:grades[1]
#age = lambda ages : ages[2]
#student.sort(key=grade,reverse=False)
#student.sort(key=age,reverse=False)
#sorted_student = sorted(student,key=grade,reverse=True)
#sorted_student = sorted(student,key=age,reverse=True)
#for i in sorted_student:
#    print(i)
#---------------------------------------------------------------------------------------------------------------
# map() = applies a function with each item in an iterables (list, tubles, etc)
# map(function,iterable)

#store = [("shirt", 20.00),
#         ("pants", 25.00),
#         ("jacket",50.00),
#         ("socks", 10.00)]
#to_euros = lambda data: (data[0], data[1]*0.82)
#to_dollar = lambda data: (data[0], data[1]/0.82)

#store_euros = list(map(to_euros, store))
#store_dollar = list(map(to_dollar, store))


#for i in store_dollar:
#    print(i)
#---------------------------------------------------------------------------------------------------------------
# Filter () = create a collection of elements from an iterable for which a function return
# filter(function, iterable)

#friend = [("Rachel", 19),
#          ("Josh", 16),
#          ("Rick", 41),
#          ("Chandler", 21),
#          ("Rose", 20),
#          ("Joey", 19)]
#age = lambda ages:ages[1] >= 18

#drinking_buddies = list(filter(age, friend))

#for i in drinking_buddies:
#    print(i)
#---------------------------------------------------------------------------------------------------------------
# reduce() = applys a function to an iterable and reduce it to a single cumulative value,
#            performes a list on the first to two elements and repeats process until 1 value remains
# reduce(functions, iterables)
#import functools

#letters = ["H","E","L","L","O"]
#word = functools.reduce(lambda x,y:x+y,letters)
#print(word)

#factorial = [5,4,3,2,1]
#multiples = functools.reduce(lambda x,y:x*y,factorial)
#print(multiples)
#---------------------------------------------------------------------------------------------------------------
# List Conprehension = A a way to create a new list with less syntax
#                      Can mimic a simple lamdba functions, easier to read
#                      list = [expression for item in iterable]
#                      list = [expression for item in iterable if conditon]
#                      list = [expression (if/else) for item in iterable]

#square = []                  #create an empty list
#for i in range(1, 11):       #create a for loo[
#    square.append(i * i)       #define what each loop is iteration should do
#print(square)
#square = [i * i for i in range(1, 11)]
#
#print(square)

#student = [100,90,80,70,60,50,40,0]
#pass_student = list(filter(lambda x:x >= 60, student))

#pass_student = [i if i >= 60 else "FAILED" for i in student ]

#print(pass_student)
#---------------------------------------------------------------------------------------------------------------
# dictionary comprehension = create dictionaries using an expression
#                            can replace for loop and simple lambda function
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditonal}
# dictionary = {key: (if/else for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}

#cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
#print(cities_in_C)

#weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
#sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
#print(sunny_weather)

#cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#desc_cities = {key: ("Warm" if value >= 40 else "Cold") for (key,value) in cities_in_F.items()}
#print(desc_cities)

#def check_temp(value):
#    if value >= 70:
#        return "Hot"
#    elif 69 >= value >= 40:
#        return "Warm"
#    else:
#        return "Cold"

#weather = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#desc_cities = {key: check_temp(value) for (key,value) in cities_in_F.items()}
#---------------------------------------------------------------------------------------------------------------
# zip(*iterables) = aggregate elements from two or more iterables (list,tuples,sets,etc)
#                   create a zip object with paired elements stored in a tuples for each elements

#username = ["Josh", "Rick", "Abellera"]
#password = ("p@ssord", "abc123", "shoot")
#login_date = ["1/1/2021","1/2/2021","1/3/2021"]
#data = list(zip(username,password,login_date))
#data = list(zip(username,password))
#data = dict(zip(username,password))

#print(data)
#for i in data:
#    print(i)

#for key,value in data.items():
#    print(key+" : "+value)
#---------------------------------------------------------------------------------------------------------------
# ***********************************************************************************
# if __name__ == '__main__'
# ***********************************************************************************
# y tho?
# 1. module can run as a standalone program
# 2. module can be imported and used in other modules

# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it is
#the initial module being run

#import module_two
#print(__name__)
#print(module_two.__name__)

#if __name__ == '__main__':
#    print("This module is being run directly")
#else:
#    print("This module is being run indirectly")

#def hello():
#    print("Hello!")
#if __name__ == '__main__':
#    hello()
#---------------------------------------------------------------------------------------------------------------
#import time

#print(time.ctime(0))        # convert a time expression in seconds since epoch to readable string
                            # epoch is when your computer time began (reference point)
#print(time.time()) # return current second since epoch

#print(time.ctime(time.time()))

#time_object = time.localtime() # Local time
#time_object = time.gmtime() #Prior to 1972, this time was called Greenwich Mean Time (GMT) but is now referred to as
# Coordinated Universal Time or Universal Time Coordinated (UTC). It is a coordinated time scale,
# maintained by the Bureau International des Poids et Mesures (BIPM). It is also known as "Z time" or "Zulu Time".
#print(time_object)

#local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)
#print(local_time)
#time_string = "20 April 2022"
#time_object = time.strftime(time_string,"%d %B, %Y")
#print(time_object)
# (year, month, days, hours, minutes, seconds, # days of a week, days of a year, dst
#time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
#time_string = time.asctime()
#time_string = time.mktime(time_tuple)
#print(time_string)
#---------------------------------------------------------------------------------------------------------------
# thread  = a flow of execution, Like separate order of instruction
#           However each tread has a turn of running to achiave cuncurrency
#           GIL = (global interpreter lock)
#           allows only one thread to hold the control of Python interpreter at any one time
# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use of multiprossesing
# io bound = program/task spends most of it's time waiting external events (user input, web scraping)
#             use multithreading

#import threading

#import time

#def washo():
#    time.sleep(3)
#    print("You finish washing up")

#def breakfast():
#    time.sleep(4)
#    print("You finist breakfast")

#def dress_up():
#    time.sleep(5)
#    print("You finish dressing up")

#x = threading.Thread(target=washo, args=())
#x.start()

#y = threading.Thread(target=breakfast, args=())
#y.start()

#z = threading.Thread(target=dress_up, args=())
#z.start()

#x.join()
#y.join()
#z.join()

#wash()
#breakfast()
#dress_up()

#print(threading.active_count())
#print(threading.enumerate())
#print(time.perf_counter())
#---------------------------------------------------------------------------------------------------------------
# deamon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for deamon threads to complete before exiting
#                 non-deamon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. backround task, garbage collection, waiting for input, long running process

#import threading
#import time

#def timer():
#    print()
#    count = 0
#    while True:
#        time.sleep(1)
#        count += 1
#        print("logged in for:", count,"seconds")

#x = threading.Thread(target=timer, daemon=True)
#x.start()
#print(x.isDaemon())
#answer = input("Do you wish to exit?"
#               "")
#---------------------------------------------------------------------------------------------------------------
#***************************************************************
# Python Multiprocessing
#***************************************************************
# multiprocessing = running tasks in a parrallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound task (waiting round)
#from multiprocessing import Process, cpu_count
#import time

#def counter(num):
#    count = 0
#    while count < num:
#        count += 1

#def main():
#    print(cpu_count())
#    a = Process(target=counter, args=(250000000,))
#    b = Process(target=counter, args=(250000000,))
#    c = Process(target=counter, args=(250000000,))
#    d = Process(target=counter, args=(250000000,))

#    a.start()
#    b.start()
#    c.start()
#    d.start()

#    a.join()
#    b.join()
#    c.join()
#    d.join()

#    print("finish in",time.perf_counter(),"seconds")

#if __name__ == '__main__':
#    main()
#---------------------------------------------------------------------------------------------------------------
#from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = servers as container to hold or contain these widgets

#window = Tk() # instantiate an instance of a windows
#window.geometry("500x500")
#window.title("Joshrick's First GUI Program")

#icon = PhotoImage(file='grey.jpg') # I Don't Really Have The appropriate File On This One : So I Pass
#window.iconphoto(True,icon)
#window.config(background="black")
#You can use the Hex value to use your prefered mixed color, that's not found with in the rainbow color
# Hex Color Picker On Google
#window.mainloop() # place window on a computer screen and also listen for events
#***************************************************************
#from tkinter import *

# Labels = an area widget that holds text and/or an image withing a window

#window = Tk()
#photo = PhotoImage(file='grey.gif')
#photo = PhotoImage(file='C:\\Users\\07\\grey.jpg') # But This One I Need A GIF OR A PNG Not A JPG File:
# Because Python Do Not Support JPG File
#label = Label(window,
#              text='Hello World',
#              font=('Arial',40,'bold'),
#              fg='green',bg='black',
#              relief=RAISED,
#              bd=10,
#              padx=20,
#              pady=20,
#              image=photo,
#              compound='bottom')# Top, Left And Right
#label.pack()
#label.place(x=0,y=0)

#window.mainloop()
#***************************************************************
#from tkinter import *
# Buttons

#window = Tk()
#count = 0
#def click():
#    global count
#    count += 1
#    print("You like the button",count,"time")
#    print("You click the button")

#photo = PhotoImage(file="images-removebg-preview.png")

#button = Button(window,
#                text="Like",
#                command=click,
#                font=("Comic Sans",30),
#                fg="white",
#                bg="Black",
#                activeforeground="white",
#                activebackground="black",
#                image=photo,
#                compound="bottom")
#button.pack()

#window.mainloop()
#***************************************************************
#from tkinter import *

# Entry Widgets = textbox that accepts a single line of user input

#def submit():
#    username = entry.get()
#    print("Hello "+username)
#    entry.config(state=DISABLED)

#def delete():
#    entry.delete(0,END)

#def backspace():
#    entry.delete(len(entry.get())-1,END)

#window = Tk()

#entry = Entry(window,
#              font=("Arial",30,),
#              background="black",
#              foreground="white")
#              #fg="white")
              #show="*")
#entry.insert(0,"Enter",)
#entry.config(state=DISABLED)
#entry.pack(side=LEFT)

#button = Button(window,
#                text="submit",
#                command=submit)
#button.pack(side=RIGHT)

#delete_button = Button(window,
#                text="delete",
#                command=delete)
#delete_button.pack(side=RIGHT)

#backspace_button = Button(window,
#                text="backspace",
#                command=backspace)
#backspace_button.pack(side=RIGHT)

#window.mainloop()
#***************************************************************
#from tkinter import *

#def display():
#    if (x.get()==1):
#        print("You agreeeeeeee")
#    else:
#        print("You Don't Agreeeeee")

#window = Tk()

#x = IntVar() # StringVar, BooleanVar

#photo = PhotoImage(file='download-removebg-preview.png')

#check_button = Checkbutton(window,
#                           text="I Agreeeee",
#                           font=("Arial",15),
#                           bg="Black",
#                           fg="BLue",
#                           activebackground="black",
#                           activeforeground="Blue",
#                           variable=x,
#                           onvalue=1, # True, Yes
#                           offvalue=0,# False, No
#                           command=display,
#                           pady=25,
#                           padx=10,
#                           image=photo,
#                           compound=LEFT)
#check_button.pack()


#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
# Radio Button = similar to checkbox, but you can only select one from a group from
#from tkinter import *

#food = ["pizza", "hamburger", "hotdog"]

#def order():
#    if (x.get()) == 0:
#        print("You Ordered Pizza")
#    elif (x.get()) == 1:
#        print("You Ordered Hamburger")
#    elif (x.get()) == 2 :
#        print("You Ordered Hotdog")
#    else:
#        print("huh??")
#window = Tk()

#pizza_ = PhotoImage(file='download__1_-removebg-preview.png')
#hamburger_ = PhotoImage(file='images__1_-removebg-preview.png')
#hotdog_ = PhotoImage(file='images__2_-removebg-preview.png')
#food_ = [pizza_,hamburger_,hotdog_]


#x = IntVar()

#for i in range(len(food)):
#    radio = Radiobutton(window,
#                        text=food[i], # add text to radiobutton
#                        variable=x, # groups radiobuttons together if they share the same variable
#                        value=i, # give each radiobutten a value
#                        fg="black",
#                        padx=25, # add padding on x-axis
#                        font=("Impact",34),
#                        image=food_[i],
#                        compound=LEFT,
#                        indicatoron=0, # Eliminate the circle indicator
#                        width=500,
#                        command=order)
#    radio.pack(anchor=W)

#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
#from tkinter import *

#def submit():
#    print("The Temperature is "+str(scale.get())+" Degree Celsius")

#window = Tk()

#fire = PhotoImage(file='download__1_-removebg-preview (1).png')
#fire_L = Label(image=fire)
#fire_L.pack()

#scale = Scale(window,from_=100,
#              to=0,
#              length=400,
#              font=("Consolas", 20),
#              orient=VERTICAL, # HORIZONTAL
#              tickinterval=10, # Adds A Numeric Indicator Value
#              #showvalue=0, #Hide Current Value, But It Depend On it's Usage
#              resolution= 1, # Increment of slider
#              troughcolor="black",
#              fg="gray",
#              bg="black")

#scale.set(50) # It is Place At A Default Value
#scale.set(((scale['from']-scale['to'])/2)+scale['to']) # This is unnessecarry but yeah
#scale.pack()

#button = Button(window,text="submit",
#                command=submit,)
#button.pack()

#ice = PhotoImage(file='download__2_-removebg-preview.png')
#ice_L = Label(image=ice)
#ice_L.pack()

#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
# listbox = A listing of selectable text item within it's own container
#from tkinter import *

#def submit():

#    food = []

#    for i in listbox.curselection():
#        food.insert(i,listbox.get(i))
#    #print(listbox.get(listbox.curselection()))
#    print("You Have Ordered :")
#    for i in food:
#        print(i)

#def Add_M():
#    listbox.insert(listbox.size(),entry.get())
#    listbox.config(height=listbox.size())

#def delete():
#    for i in reversed(listbox.curselection()):
#        listbox.delete(i)
#        listbox.config(height=listbox.size())

    #foods = []          tried creating one for my self and it work!, but not entirely :(
    #for i in listbox.curselection():
    #    foods.insert(i,listbox.delete(i))


#window = Tk()

#listbox = Listbox(window,bg="#c1c2c7",
#                  fg="black",
#                  font=("Constantia",20),
#                  width=10,
#                  selectmode=MULTIPLE)
#listbox.pack()

#listbox.insert(1,"pizza")
#listbox.insert(1,"pasta")
#listbox.insert(1,"garlic bread")
#listbox.insert(1,"soup")
#listbox.insert(1,"salad")

#listbox.config(height=listbox.size())

#entry = Entry(window)
#entry.pack()

#submit_Button = Button(window,
#                       text="Submit",
#                       command=submit)
#submit_Button.pack()

#addButton = Button(window,text="Add",
#              command=Add_M)
#addButton.pack()

#delete_B = Button(window,
#                  text="Delete",
#                  command=delete)
#delete_B.pack()

#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
#from tkinter import *
#from tkinter import messagebox # Import Message Box Library: Submodule

#def click():
    #messagebox.showinfo(title='Info Message Box',message='If Not Given, Info Will Be Stolen',)

    #messagebox.showwarning(title='WARNING',message='If Not Given, Info Will Be Stolen', )

    #while True:
    #messagebox.showerror(title='Error',message='Something Is Wrong With You', )

    #while True:
    #if messagebox.askokcancel(title='Ok/Cancel',message='Do It'):
    #    print("Awesome :(")
    #else:
    #    print("Boo"

    #if messagebox.askyesno(title='Yes/No', message='Do You Get Some Bitches'):
    #    print("You Are Gay :(")
    #else:
    #    print("GIGA CHAD")

    #if messagebox.askretrycancel(title='Retry', message='Do You Want To Retry'):
    #    print("Nice And Fresh")
    #else:
    #    print("Ok")

    #print(messagebox.askquestion(title='Question', message='Do You Get Some Bitches'))
    #user = (messagebox.askquestion(title='Question', message='Do You Get Some Bitches'))
    #if (user == 'yes'):
    #    print("Gayyyyy!")
    #else:
    #    print("Chad")
    #print(messagebox.askyesnocancel(title='Yes/No/Cancel',message='Do You Like It Cold?'))
#    user = messagebox.askyesnocancel(title='Yes/No/Cancel',message='Do You Like It Cold?')#icon='warning',info,error)
#    if (user == True):
#        print("Nice Choice")
#    elif (user == False):
#        print("Then Hot It is")
#    else:
#        print("Then What Do You Like?")

#window = Tk()

#button = Button(window,
#                text="Click Me",
#                command=click)
#button.pack()

#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
#from tkinter import *
#from tkinter import colorchooser #submodule

#def Choose_Color():
#    color = colorchooser.askcolor() # Hassle
#    #print(color)
#    color_Hex = color[1]
#    #print(color_Hex)
#    window.config(bg=color_Hex)

    #window.config(bg=color[1]) # Lvl 2 Middle

    #window.config(bg=colorchooser.askcolor()[1]) # Lvl 3 Easier


#window = Tk()

#window.geometry('420x420')

#button = Button(window,text='Color Chooser',
#                command=Choose_Color,
#                bg='#6f53ee')
#button.pack()

#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
# Text Widget = function like a text area, you can enter multiple lines of text
#from tkinter import *

#def submit():
#    input = text.get("1.0",END)
#    print(input)

#window = Tk()
#text = Text(window,
#            bg='Light Yellow',
#            font=("Ink Free",25),
#            height=8,
#            width=20,
#            pady=20,
#            padx=20)
#text.pack()

#button = Button(window,text='submit',command=submit)
#button.pack()
#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
# Opening And Closing File
#from tkinter import *
#from tkinter import filedialog

#def openfile():
#    filepath = filedialog.askopenfilename(initialdir="C:\\Users//07\PycharmProjects\\pythonProject\\HelloWorld",
#                                          title="OpenFile",
#                                          filetypes=(("text files","*.txt"),
#                                          ("all file","*.*")))
    #print(filepath)
#    file = open(filepath,"r")
#    print(file.read())
#    file.close()

#window = Tk()
#button = Button(window,text="Open",
#                command=openfile)
#button.pack()
#window.mainloop()
# ***********************************************************************************
#from tkinter import *
#from tkinter import filedialog

#def save():
#    file = filedialog.asksaveasfile(initialdir='C:\\Users\\07\PycharmProjects\\pythonProject\\HelloWorld',
#                                    defaultextension=',txt',
#                                    filetypes=[
#                                        ("Text file",".txt"),
#                                        ("HTML",".html"),
#                                        ("All files", ".*"),
#                                    ])
#    if file is None:
#        return
#    #textfile = str(text.get(1.0,END))
#    textfile = input("Input:"
#                    "")
#    file.write(textfile)
#    file.close()

#window = Tk()
#button = Button(window,text="Save",
#                command=save)
#button.pack()
#text = Text(window,font=("Ink Free",20),
#            width=25,
#            height=10,
#            bg="Light yellow")
#text.pack()
#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
#from tkinter import *

#def openFile():
#    print("Opened File")

#def saveFile():
#    print("Save File")

#def cut():
#    print("Cut")

#def copy ():
#    print("Copy")

#def paste():
#    print("Paste")


#window = Tk()

#menubar = Menu(window)
#window.config(menu=menubar,)

#filemenu = Menu(menubar,tearoff=0)
#menubar.add_cascade(label="File",menu=filemenu)
#filemenu.add_command(label="Open",command=openFile)
#filemenu.add_command(label="Save",command=saveFile)
#filemenu.add_command(label="Exit",command=quit) # Or You can go the hard way: creat a function
#filemenu.add_separator()

#editmenu = Menu(menubar,tearoff=0)
#menubar.add_cascade(label="Edit",menu=editmenu)
#editmenu.add_command(label="Cut",command=cut)
#editmenu.add_command(label="Copy",command=copy)
#editmenu.add_command(label="Paste",command=paste)
#editmenu.add_separator()


#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
# Frame = a rectangular container to a group and hold a widgets
#from tkinter import *
#window = Tk()

#frame = Frame(window,bg="pink",bd=5,relief="sunken")
#frame.pack()

#Button(frame,text="W",font=("Consolas",20),width=3).pack(side=TOP)
#Button(frame,text="A",font=("Consolas",20),width=3).pack(side=LEFT)
#Button(frame,text="S",font=("Consolas",20),width=3).pack(side=LEFT)
#Button(frame,text="D",font=("Consolas",20),width=3).pack(side=LEFT)


#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
# Creat A New Window And Destroy
#from tkinter import *

#def create_window():
#    new_window = Tk() # Toplevel() = new window 'on top' of other window. linked to 'bottom' window
                      # Tk() = A New Independant window
#    old_window.destroy()  # It will close or destroy the old window
#old_window = Tk()

#Button(old_window,text="Creat New Window",command=create_window).pack()


#old_window.mainloop()
#---------------------------------------------------------------------------------------------------------------
#from tkinter import *
#from tkinter import ttk

#window = Tk()

#notebook = ttk.Notebook(window) # A widget that manages collection of window and displays

#tab_1 = Frame(notebook) # new frame for tab 1
#tab_2 = Frame(notebook) # new frame for tab 2

#notebook.add(tab_1,text="Tab 1",)
#notebook.add(tab_2,text="Tab 2",)
#notebook.pack(expand=True,fill="both") # This Expand To Fill Any Space Not Otherwise used
                                       # fill = will fill space on x and y axis
#Label(tab_1,text="This is tab 1",width=50,height=25).pack()
#Label(tab_2,text="This is tab 2",width=50,height=25).pack()

#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
#from tkinter import *
# grid() = geometry manager that organizes the widgets in a table-like sturcture in a parent class


#window = Tk()

#title_label = Label(window,text="Profile",font=("Arial",15)).grid(row=0,column=0,columnspan=1)

#first_name = Label(window,text="First Name: ",width=10,fg="Blue").grid(row=1,column=0)
#first_name_entry = Entry(window).grid(row=1 ,column=1)

#last_name = Label(window,text="Last Name:",width=10,fg="green").grid(row=2,column=0)
#last_name_entry = Entry(window).grid(row=2 ,column=1)

#email_name = Label(window,text="Email: ",width=10,fg="red").grid(row=3,column=0)
#email_name_entry = Entry(window).grid(row=3 ,column=1)

#submit = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)

#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
#from tkinter import *
#from tkinter.ttk import *
#import time

#def start():             # Lvl 1 Easier
#    tasks = 10
#    x = 0
#    while (x< tasks):
#        time.sleep(1)
#        bar['value']+=10
#        x += 1
#        percent.set(str(int((x/tasks)*100))+"%")
#        window.update_idletasks()
#    print("Finish")

#def start():            # Lvl 2 Harder
#    tasks = 10
#    x = 0
#    while (x< tasks):
#        time.sleep(1)
#        bar['value']+=10
#        x += 1
#        percent.set(str(int((x/tasks)*100))+"%")
#        text.set(str(x)+"/"+str(tasks)+"Task Completed")
#        window.update_idletasks()
#def start():            # Change Task To GB Or A Different Variation
#    GB = 100
#    Download = 0
#    speed = 1
#    while (Download< GB):
#        time.sleep(0.05)
#        bar['value']+=(speed/GB)*100
#        Download += speed
#        percent.set(str(int((Download/GB)*100))+"%")
#        text.set(str(Download)+"/"+str(GB)+" GB Completed")
#        window.update_idletasks()
#window = Tk()

#percent = StringVar()
#text = StringVar()

#bar = Progressbar(window,orient=HORIZONTAL,length=300,)
#bar.pack(padx=10)

#percentL = Label(window,textvariable=percent).pack()
#taskL = Label(window,textvariable=text).pack()

#button = Button(window,text="Download",command=start).pack()

#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
# canvas = widget that is used to draw graphs, plots, images in window
#from tkinter import *

#window = Tk()

#canvas = Canvas(window,height=500,width=500)
#canvas.create_line(0,0,500,500,fill="BLue",width=4)
#canvas.create_line(0,500,500,0,fill="red",width=4)
#canvas.create_rectangle(50,50,200,200,fill="red",width=4)
#points = [250,0,500,500,0,500]
#canvas.create_polygon(points,fill="black",width=4,outline="red")
#canvas.create_arc(0,0,500,500,fill="Green",style=PIESLICE,start=270,extent=180) # Arc,Chord
#canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
#canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
#canvas.create_oval(190,190,310,310,fill="white",outline="black",width=5)
#canvas.create_oval(220,220,270,270,fill="white",outline="black",width=5)  #close enough
#canvas.pack()
#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
#The bind() method of Python's socket class assigns an IP address and a port number to a socket instance.
# The bind() method is used when a socket needs to be made a server socket. As server programs listen on published ports,
# it is required that a port and the IP address to be assigned explicitly to a server socket.
# Or in short it assign it to a key and takes two argument (Event,Function)
#from tkinter import *

#def doSomething(event):
#    label.config(text=event.keysym)
#window = Tk()

#window.bind("<Key>",doSomething)

#label = Label(window,font=("Helvetica",100))
#label.pack()

#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
#from tkinter import *

#def doSomething(event):
#    print("Mouse Coordinate: "+str(event.x)+","+str(event.y))

#window = Tk()

#window.bind("<Button-1>",doSomething) # Left Mouse Click
#window.bind("<Button-2>",doSomething) #Middle Cursor
#window.bind("<Button-3>",doSomething) # Right Mouse Click
#window.bind("<ButtonRelease>",doSomething) # Execute after releasing the mouse left,right or middle cursor
#window.bind("<Enter>",doSomething) # enter window
#window.bind("<Leave>",doSomething) # leave window
#window.bind("<Motion>",doSomething) # Moving the cursor or mouse

#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
#from tkinter import *

#def drag_start(event):
#    widget = event.widget
#    widget.startX = event.x
#    widget.startY = event.y

#def drag_motion(event):
#    widget = event.widget
#    x = widget.winfo_x() - widget.startX + event.x
#    y = widget.winfo_y() - widget.startY + event.y
#    widget.place(x=x,y=y)


#window = Tk()

#label = Label(window,bg="red",width=10,height=5)
#label.place(x=0,y=0)

#label2 = Label(window,bg="blue",width=10,height=5)
#label2.place(x=100,y=100)        # I am really dump fr fr :(
                                 # the definiton of have an open mind

#label.bind("<Button-1>",drag_start)
#label.bind("<B1-Motion>",drag_motion)

#label2.bind("<Button-1>",drag_start)
#label2.bind("<B1-Motion>",drag_motion)

#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
#from tkinter import *
# Picture moving

#def up(event):
#    foodL.place(x=foodL.winfo_x(), y=foodL.winfo_y()-10)

#def down(event):
#    foodL.place(x=foodL.winfo_x(), y=foodL.winfo_y()+10)

#def left(event):
#    foodL.place(x=foodL.winfo_x()-10, y=foodL.winfo_y())

#def right(event):
#    foodL.place(x=foodL.winfo_x()+10, y=foodL.winfo_y())

#window = Tk()

#window.geometry("500x500")
#window.bind("<w>",up)
#window.bind("<a>",left)
#window.bind("<d>",right)
#window.bind("<s>",down)
#window.bind("<Up>",up)         # Didn't feel like fixing it
#window.bind("<Down>",left)     # So Yeah move forward
#window.bind("<Left>",right)    #
#window.bind("<Right>",down)    #


#food = PhotoImage(file='images__2_-removebg-preview.png')
#foodL = Label(window,image=food)
#foodL.place(x=0,y=0)


#window.mainloop()
# ***********************************************************************************
# Part 2 Canvas moving

#from tkinter import *

#def up(event):
#    canvas.move(myphoto,0,-10)
#def down(event):
#    canvas.move(myphoto,0,10)

#def left(event):
#    canvas.move(myphoto,-10,0)

#def right(event):
#    canvas.move(myphoto,10,0)


#window = Tk()

#window.bind("<w>",up)
#window.bind("<a>",left)
#window.bind("<d>",right)
#window.bind("<s>",down)
#window.bind("<Up>",up)
#window.bind("<Left>",left)
#window.bind("<Right>",right)
#window.bind("<Down>",down)

#photo = PhotoImage(file='images__2_-removebg-preview.png')

#canvas = Canvas(window,width="500",height="500")
#canvas.pack()

#myphoto = canvas.create_image(0,0,image=photo,anchor=NW)

#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
# 2D Animation :(
#from tkinter import *
#import time

#WIDTH = 500 # If You Don't plan on changing it's size
#HEIGHT = 500 # Edit the size using this
#yVelo = 1
#xVelo = 1
#window = Tk()

#canvas = Canvas(window,width=WIDTH,height=HEIGHT)
#canvas.pack()

#space = PhotoImage(file=)# could't find a png background
#spaceB = canvas.create_image(0,0,image=space,anchor=NW)

#ufo = PhotoImage(file='download-removebg-preview.png')
#my_ufo = canvas.create_image(0,0,image=ufo,anchor=NW)

#image_width = ufo.width()
#image_height = ufo.height()

#while True:
#    coordinate = canvas.coords(my_ufo)
#    print(coordinate)
#    if (coordinate[0]>=(WIDTH-image_width) or coordinate[0]<0):
#        xVelo = -xVelo
#    if (coordinate[1]>=(HEIGHT-image_height) or coordinate[1]<0):
#        yVelo = -yVelo
#    canvas.move(my_ufo,xVelo,yVelo)
#    window.update()
#    time.sleep(0.01)


#window.mainloop()
#---------------------------------------------------------------------------------------------------------------
# Multiple 2D Animation
from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_Ball = Ball(canvas,0,0,100,1,1,"white")

while True:
    volley_Ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop

class Ball:

    def __int__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
        self.canves = canvas
        self.image = canvas.creat_oval(x,y,diameter,diameter,fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinate = self.canves.coords(self.image)
        print(coordinate)

        self.canves.move(self.image,self.xVelocity,self.yVelocity )
