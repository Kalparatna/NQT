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

candidates = int(input())

candidate_skills = []  
for i in range(candidates):
    subset_skills = input().split()  
    candidate_skills.append(subset_skills)  

