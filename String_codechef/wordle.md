# Wordle

Chef has invented a modified version of Wordle.

## Game Description

There is a hidden word `S` and a guess word `T`, both of length 5.
Chef defines a string `M` to determine the correctness of the guess word. For the `i`-th index:

*   If the guess at the `i`-th index is correct, the `i`-th character of `M` is `G`.
*   If the guess at the `i`-th index is wrong, the `i`-th character of `M` is `B`.

Given the hidden word `S` and guess `T`, the task is to determine the string `M`.

## Input Format

*   The first line contains `T`, the number of test cases.
*   Each test case consists of two lines:
    *   The first line contains the string `S` - the hidden word.
    *   The second line contains the string `T` - the guess word.

## Output Format

For each test case, print the value of string `M`.

You may print each character of the string in uppercase or lowercase (for example, the strings `BgBgB`, `BGBGB`, `bgbGB`, and `bgbgb` will all be treated as identical).

## Constraints

*   `1 <= T <= 1000`
*   `|S| = |T| = 5`
*   `S`, `T` contain uppercase English alphabets only.

## Sample 1:

### Input

```
3
ABCDE
EDCBA
ROUND
RINGS
START
STUNT
```

### Output

```
BBGBB
GBBBB
GGBBG
```

### Explanation

**Test Case 1:**
Given `S = ABCDE` and `T = EDCBA`. The string `M` is:
*   Comparing the first indices, `A ≠ E`, thus, `M[1] = B`.
*   Comparing the second indices, `B ≠ D`, thus, `M[2] = B`.
*   Comparing the third indices, `C = C`, thus, `M[3] = G`.
*   Comparing the fourth indices, `D ≠ B`, thus, `M[4] = B`.
*   Comparing the fifth indices, `E ≠ A`, thus, `M[5] = B`.
Thus, `M = BBGBB`.

**Test Case 2:**
Given `S = ROUND` and `T = RINGS`. The string `M` is:
*   Comparing the first indices, `R = R`, thus, `M[1] = G`.
*   Comparing the second indices, `O ≠ I`, thus, `M[2] = B`.
*   Comparing the third indices, `U ≠ N`, thus, `M[3] = B`.
*   Comparing the fourth indices, `N ≠ G`, thus, `M[4] = B`.
*   Comparing the fifth indices, `D ≠ S`, thus, `M[5] = B`.
Thus, `M = GBBBB`.

## Solution (Python)

```python
t = int(input())

for _ in range(t):
    s1 = input()
    s2 = input()
    res = []
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            res.append("G")
        else:
            res.append("B")
    print("".join(res))