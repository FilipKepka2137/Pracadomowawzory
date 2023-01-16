from math import pi



class Matematycznewzorkipracadomowa:
    def __init__(self,r,h,pp,pb,x,y,z):
        self.r = r
        self.h = h
        self.pp = pp
        self.pb = pb
        self.x = x
        self.y = y
        self.z = z



    def obj_szescian(self):
        print(self.x**3)

    def p_szescianu(self):
        print(6*self.x**2)

    def pc_szescianu(self):
        print(6*self.x**2)



    def obj_prostopadloscian(self):
        print(self.x*self.y*self.z)

    def p_prostopadloscian(self):
        print(2*self.x*self.y+2*self.x*self.z+2*self.y*self.z)

    def pc_prostopadloscianu(self):
        print(2*self.x*self.y+2*self.x*self.z+2*self.y*self.z)



    def obj_graniastoslup(self):
        print(self.pp*self.h)

    def p_graniastoslup(self):
        print(2*self.pp+self.pb)

    def pc_graniastoslup(self):
        print(2*self.x*self.y+2*self.y*self.z)



    def obj_ostroslup(self):
        print(1/3 * self.pp * self.h)

    def p_ostroslup(self):
        print(self.pp+self.pb)