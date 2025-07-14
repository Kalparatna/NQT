'''
Lohia, Gosu and Prince are footballers. Lohia and Gosu are strikers while Prince is a goalkeeper. 
You as the coach held a practice session of penalty shootouts to improve the performance of the strikers. 
Your task is to find the maximum goal scorer between the two.

Google

170

Lohia, Gosu and Prince energy is denoted by X, Y and Z respectively. 
For every goal scored the energy of the respective player is decreased by 1 and after every save Prince energy is decreased by 1. 
Strikers will be able to score the goal if Prince energy is a factor of their energy otherwise not.

The session ends when Prince's energy reaches 1.

Assume same player can try for goals repeatedly and they both try to increase number of goals in totality. 
Lohia being a junior player is always favoured for penalty kick.

Input:

The first line of input contains an integer T denoting the number of test cases. 
Each test case contains energy 3 integers X, Y & Z, denoting the energies respectively.
ex - INPUT:

2
10 15 5
12 9 3


Output:

For each test case print the number of goals scored by Lohia and Gosu respectively.
ex- output for above test cases
1 0
1 1

'''
def max_goal_scorer(test_cases):
    results = []
    for X, Y, Z in test_cases:
        lohia_goals, gosu_goals = 0, 0
        
        while Z > 1:
            if X % Z == 0:
                lohia_goals += 1
                X -= 1
            elif Y % Z == 0:
                gosu_goals += 1
                Y -= 1
            Z -= 1
        
        results.append(f"{lohia_goals} {gosu_goals}")
    
    return "\n".join(results)

# Reading input
def main():
    T = int(input())
    test_cases = [tuple(map(int, input().split())) for _ in range(T)]
    print(max_goal_scorer(test_cases))

if __name__ == "__main__":
    main()
