'''
2. Minimum Team Selection to Cover Required Skills
Problem Statement:
You are given a list of required skills and a list of candidates, where each candidate has a subset of skills. Your task is to find the smallest possible team such that all required skills are covered.

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

Input:
a b c
3
a
b c
c
Output:
0 1

'''
#without inbuilt Funcitons
def smaller_sufficient_team(req_skills, people):
    # Convert required skills to a list and map each skill to an index
    skill_index = {skill: i for i, skill in enumerate(req_skills)}
    total_skills = len(req_skills)
    n = len(people)

    # Convert each person's skill set to a bitmask
    people_masks = []
    for person in people:
        mask = 0
        for skill in person:
            if skill in skill_index:
                mask |= 1 << skill_index[skill]
        people_masks.append(mask)

    # Initialize DP table, key: skill_mask, value: list of people indices
    dp = {0: []}

    for i in range(n):
        person_mask = people_masks[i]
        # We make a copy of current dp keys to avoid modifying while iterating
        new_dp = dict(dp)
        for skill_mask in dp:
            combined = skill_mask | person_mask
            if combined not in new_dp or len(dp[skill_mask]) + 1 < len(new_dp[combined]):
                new_dp[combined] = dp[skill_mask] + [i]
        dp = new_dp

    full_mask = (1 << total_skills) - 1
    return dp[full_mask]


#With Funtion

def smaller_sufficient_team(req_skills, people):
    from itertools import combinations

    required = set(req_skills)
    n = len(people)

    people_skills = [set(person) for person in people]
    min_team = list(range(n))

    for team_size in range(1, n+1):
        for team_indices in combinations(range(n), team_size):
            team_skills = set()
            for i in team_indices:
                team_skills|= people_skills[i]
            
            if required.issubset(team_skills):
                if len(team_indices) < len(min_team):
                    min_team = list(team_indices)
                break
        if len(min_team) <= team_size:
            break
    
    return min_team

if __name__ == "__main__":
    req_skills = input().strip().split()
    n  = int(input())
    people = [input().strip().split()for _ in range(n)]

    result =  smaller_sufficient_team(req_skills, people)
    print(" ".join(map(str, result)))
