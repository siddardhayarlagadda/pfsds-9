class Sample:
    def Circle(self,a=0,b=0,c=0):
        self.a=a
        self.b=b
        self.c=c
        if(a!=0) and (b==0) and (c==0):
            print("Area of circle: ",3.14*(a*a))
            print("Perimeter of circle",2*3.14*a)
        elif(a!=0) and (b!=0) and (c==0):
            print("Area of Rectangle: ", a * b)
            print("Perimeter of Rectangle", 2 * (a+b))
        elif(a!=0) and (b!=0) and (c!=0):
            print("Area of Triangle: ", 0.5 * b * c)
            print("Perimeter of triangle", a + b + c)
        else:
            print("invalid")
class Main(Sample):
    def Calls(self):
        pass

ob=Main()
ob.Circle(10)
ob.Circle(4,5)
ob.Circle(2,3,8)