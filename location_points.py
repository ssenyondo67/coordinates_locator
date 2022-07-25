import math
import string

# finding square of 
def square(x):
    return x*x

class Point:

    def __init__(self,x,y) -> None:

        self.__X =x
        self.__Y =y

    def get_x(self):
        return self.__X

    def get_y(self):
        return self.__Y
    
    def distance_from_xy(self,x,y):
        distance=math.sqrt(square(x-self.__X)+square(y-self.__Y))
        return distance
    
    def distance_from_point(self,object):

        distance=math.sqrt(square(self.__X-object._Point__X)+  square(self.__Y-object._Point__Y))
        return distance

object1=Point(2.1,3.1)
print(object1.get_x())
print(object1.distance_from_xy(1.0,2.0))

print(object1.distance_from_point(Point(1.0,2.0)))

class traingle:
      
    def __init__(self,object1,object2,object3) -> None:
        self.__object_list=[]
        self.__object_list.append(object1)
        self.__object_list.append(object2)
        self.__object_list.append(object3)


        
    def perimeter(self):
        object1=self.__object_list[0]
        object2=self.__object_list[1]
        object3=self.__object_list[2]
        a= math.sqrt(square(object1._Point__X-object2._Point__X)+  square(object1._Point__Y-object2._Point__Y))  
        b= math.sqrt(square(object1._Point__X-object3._Point__X)+  square(object1._Point__Y-object3._Point__Y))  
        h= math.sqrt(square(object2._Point__X-object3._Point__X)+  square(object2._Point__Y-object3._Point__Y))  
        return a+b+h

traingle =traingle(Point(17,-20,),Point(20,17),Point(4,-20))
print("the perimeter is =  ",traingle.perimeter())