from turtle import Turtle#from turtle module import Turtle class
import random
initial_speed=5
increment_speed=10
colorss=['red','green','blue','maroon','purple','yellow']
class createcars:
    def __init__(self):
        # super().__init__()
        self.car_len=[]
        self.car_speed=initial_speed#the attribute car_speed of this class is initialized to initial_speed
    def create_cars(self):
        k=random.randint(1,6)#a number is picked up at random
        if k==1:#and if the numbers equates to 1 only then will a rectangular shaped turtle(car) be created,else there will be so many
            #turtles that it will be impossible to move forward
            # super().__init__()
            sach=Turtle("square")#Turtle is set to square shape here
            # self.shape('square')
            sach.color(random.choice(colorss))#then random color amongst the lisst of colors is chosen
            sach.shapesize(stretch_len=2,stretch_wid=1)#then the shape of this Turtle object is set to a particular length and width
            #using the shapesize method of Turtle class
            sach.penup()#pen is made up so that the turtle doesnot leave a line behind while it moves ahead
            # sach.hideturtle()
            y_ran=random.randint(-230,250)#now a random integer between -230 to 250 is chosen
            sach.goto(300,y_ran)#now the x and y coordinate is set and then turtle is sent there using goto method
            self.car_len.append(sach)#lastly the turtle is appended to car_len list which is an attibute of the createcars class
    def move(self):#now this method will run through every item of car_len list of createcars class and will move each of the turtle item backward
        for i in self.car_len:
            i.backward(self.car_speed)
    def increment_speed(self):#now by the end of every level,the speed of each of the car items needs to be increased
        self.car_speed+=increment_speed#and the speed of the car is incremented at every stage of the level


        