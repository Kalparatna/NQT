#Function Overriding  :IF child class is not satisfied with properties of 
#parent class then it rewrite the function in child class.
#only method overriding is possible . varible overriding is at run time (rum time memory allocation)


class Ambani:
    def __init__(self):
        print("Cash gold")

    def properties(self):
        print("Proeperties")

    def bike(self):
        print("Splender+")

    
class child(Ambani):

    def bike(self):
        print("Avenger")

C = child()
C.properties()
C.bike()
