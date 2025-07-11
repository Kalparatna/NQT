'''
3. Minimum Team Selection to Cover Required Skills

Problem Statement: 3

You are given a list of required skills and a list of candidates, where each candidate has a subset of skills. 
Your task is to find the smallest possible team such that all required skills are covered.

You will be given:
1. Required skills list
2. Number of candidates (N)
3. Skillsets of N candidates
Return the indices of selected candidates forming the smallest team.
Example:
Input:
a b c d
4
a b
b c
c d
d
Output:
0 2

'''
required_skill = input().split()
n = int(input())

skill_map = {}
for i, skill in enumerate(required_skill):
    skill_map[skill] = i

candidate_masks = []
for _ in range(n):
    skills = input().split()
    mask = 0
    for s in skills:
        if s in skill_map:
            mask |= 1 << skill_map[s]
    candidate_masks.append(mask)

dp = {0: []}  # key = skill bitmask, value = list of indices

for i in range(n):
    new_dp = {}
    for skill_set in dp:
        new_set = skill_set | candidate_masks[i]
        team = dp[skill_set] + [i]
        if new_set not in dp or len(dp[new_set]) > len(team):
            new_dp[new_set] = team
    for k in new_dp:
        dp[k] = new_dp[k]

full_mask = (1 << len(required_skill)) - 1
print(*dp[full_mask])

