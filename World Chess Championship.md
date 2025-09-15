# World Chess Championship Prize Money Calculation

## Problem Description

The World Chess Championship 2022 features 14 Classical games between Chef and Carlsen. Each game can result in a win for Carlsen ('C'), a win for Chef ('N'), or a draw ('D').
- A win earns 2 points.
- A loss earns 0 points.
- A draw earns 1 point for each player.

The total prize pool of the championship is `100 * X`.

**Prize Distribution Rules:**
1.  **If one player has strictly more points:** The player with more points is declared the champion and receives `60 * X` as prize money. The loser receives `40 * X`.
2.  **If total points are tied:** The defending champion, Carlsen, is declared the winner. In this case, the winner (Carlsen) receives `55 * X`, and the loser (Chef) receives `45 * X`.

Given the results of all 14 games, the task is to output the prize money Carlsen receives.

## Input Format

The first line of input contains an integer `T`, denoting the number of test cases.
Each test case consists of two lines:
- The first line contains an integer `X`, where the total prize pool is `100 * X`.
- The second line contains a string of length 14, representing the results of the match. The string consists of characters 'C' (Carlsen wins), 'N' (Chef wins), and 'D' (Draw).

## Output Format

For each test case, output in a single line the total prize money won by Carlsen.

## Constraints

- `1 <= T <= 1000`
- `1 <= X <= 10^6`
- `|S| = 14` (length of the results string)
- `S` contains only characters 'D', 'C', 'N'.

## Sample Input

```
4
100
CCCCCCCCCCCCCC
400
CDCDCDCDCDCDCD
30
DDCCNNDDDCCNND
1
NNDNNDDDNNDNDN
```

## Sample Output

```
6000
24000
1650
40
```

## Explanation of Sample Cases

**Test Case 1:**
- `X = 100`
- `S = "CCCCCCCCCCCCCC"` (Carlsen won all 14 games)
- Carlsen's score: `14 * 2 = 28`
- Chef's score: `14 * 0 = 0`
- Carlsen has more points, so he gets `60 * X = 60 * 100 = 6000`.

**Test Case 2:**
- `X = 400`
- `S = "CDCDCDCDCDCDCD"` (Carlsen won 7 games, drew 7 games)
- Carlsen's score: `7 * 2 (wins) + 7 * 1 (draws) = 14 + 7 = 21`
- Chef's score: `7 * 0 (losses) + 7 * 1 (draws) = 0 + 7 = 7`
- Carlsen has more points, so he gets `60 * X = 60 * 400 = 24000`.

**Test Case 3:**
- `X = 30`
- `S = "DDCCNNDDDCCNND"`
- Let's count wins and draws:
    - Carlsen wins ('C'): 4
    - Chef wins ('N'): 4
    - Draws ('D'): 6
- Carlsen's score: `4 * 2 (wins) + 6 * 1 (draws) = 8 + 6 = 14`
- Chef's score: `4 * 2 (wins) + 6 * 1 (draws) = 8 + 6 = 14`
- Scores are tied. Carlsen is declared the winner, but due to the tie, he receives `55 * X = 55 * 30 = 1650`.

**Test Case 4:**
- `X = 1`
- `S = "NNDNNDDDNNDNDN"`
- Let's count wins and draws:
    - Carlsen wins ('C'): 0
    - Chef wins ('N'): 8
    - Draws ('D'): 6
- Carlsen's score: `0 * 2 (wins) + 6 * 1 (draws) = 6`
- Chef's score: `8 * 2 (wins) + 6 * 1 (draws) = 16 + 6 = 22`
- Chef has more points. Carlsen is the loser, so he gets `40 * X = 40 * 1 = 40`.

## Solution (Python)

```python
t = int(input())
for _ in range(t):
    x = int(input())
    s = input()
    
    carlsen_wins = 0
    chef_wins = 0
    draws = 0
    
    for game_result in s:
        if game_result == "C":
            carlsen_wins += 1
        elif game_result == "N":
            chef_wins += 1
        else: # game_result == "D"
            draws += 1
    
    carlsen_score = (2 * carlsen_wins) + (1 * draws) 
    chef_score = (2 * chef_wins) + (1 * draws) 
    
    win_amount = 0
    if carlsen_score > chef_score:
        win_amount = 60 * x 
    elif carlsen_score < chef_score:
        win_amount = 40 * x
    else: # carlsen_score == chef_score
        win_amount = 55 * x
        
    print(win_amount)