
class A:
    def __init__(self, x):
        self.x = x
    
    def print_x(self):
        print("A: ",self.x)

class B(A):
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y

    def print_y(self):
        print("B: ", self.y)

class C(A):
    def __init__(self, x, z):
        super().__init__(x)
        self.z = z
    
    def print_z(self):
        print("C: ",self.z )

class D(B, C):
    def __init__(self, x, y ,z, w):
        super(B, self).__init__(x, y)  # Call B's constructor explicitly
        C.__init__(self, x, z)  # Call C's constructor explicitly
        self.z = z
        self.w = w
        self.y = y
        

    def print_w(self):
        print("D: ", self.w)

O = D(1,2,3,4)
O.print_x()
O.print_y()
O.print_z()
O.print_w()