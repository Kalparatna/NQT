class Cricket:
    def __init__(C, Player, Runs, Wickets):
        C.Player = Player
        C.Runs = Runs
        C.Wickets = Wickets

Stats = Cricket('Rohit', 5000, 50)
Stats1 = Cricket('Virat', 6000, 30)

print( Stats.C)
print(Stats1.Player, Stats1.Runs, Stats1.Wickets)