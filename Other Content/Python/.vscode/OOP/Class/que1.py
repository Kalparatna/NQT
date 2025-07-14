class Team:
    def __init__(self, C, P, m, A, b , bl):
        self.Country_name = C
        self.NameofPlayer = P
        self.matches = m
        self.age = A
        self.batting = b
        self.bowling = bl


    def show(self):
        print(self.Country_name, "\t", self.NameofPlayer, "\t", self.matches, "\t", self.age, "\t", self.batting, "\t", self.bowling)
        
       
p1 = Team("India", "Sachin", 295, 30, 45.51, 53.00)
p2 = Team("Austrelia", "Rickey", 160, 28, 41.00, 67.00)
p3 = Team("India", "Saurav", 230, 31, 40.95, 30.00)

print("Country Name ",  "\t Name ", "\t Mathces " "\t Age ",  "\t BattingAvg",  "\t BowlingAvg" )

p1.show()

p2.show()

p3.show()