'''
Q2)Problem Statement: Instant Runoff Voting System
Description:
There are 5 candidates (A, B, C, D, E) participating in an election. Each voter ranks all 5 candidates in order of preference.

The election follows the Instant Runoff Voting (IRV) system:

Each voter's first preference is initially counted as their vote.
If any candidate receives more than 50% of the votes, they are declared the winner.
If no candidate has more than 50% of the votes, the candidate with the fewest first-choice votes is eliminated.
The votes for the eliminated candidate are redistributed to the next preferred candidate still in the race.
This process repeats until a candidate secures more than 50% of the votes.

Input Format:
The first line contains two integers N (number of voters) and M (number of candidates, always 5).
The next N lines contain a string of M uppercase letters representing the voter's ranked preferences.
Output Format:
Print:
Winner <candidate name>
where <candidate name> is the candidate who wins the election.

Constraints:
1≤N≤1001
M=5 (always 5 candidates)
Candidates' names are always uppercase letters: A, B, C, D, E.
Each voter provides a valid ranking containing all 5 candidates exactly once.

Example Input 1:

45 5
ABCED
BCDAE
ACBED
CBDEA

Winner A


'''

from collections import defaultdict

def instant_runoff_voting(n, ballots):
    candidates = {'A', 'B', 'C', 'D', 'E'}
    
    while True:
        vote_count = defaultdict(int)
        
        # Count first-choice votes for remaining candidates
        for ballot in ballots:
            for candidate in ballot:
                if candidate in candidates:
                    vote_count[candidate] += 1
                    break  # Count only the first valid choice
        
        # Check if any candidate has > 50% votes
        total_votes = sum(vote_count.values())
        for candidate, count in vote_count.items():
            if count > total_votes / 2:
                print(f"Winner {candidate}")
                return
        
        # Find the candidate(s) with the fewest votes
        min_votes = min(vote_count.values())
        eliminated_candidates = {c for c in vote_count if vote_count[c] == min_votes}
        
        # Remove the eliminated candidate(s) from the race
        candidates -= eliminated_candidates

# Taking input from the user
n, m = map(int, input().split())  # Read number of voters (N) and candidates (M)
ballots = [input().strip() for _ in range(n)]  # Read the ranked ballots

instant_runoff_voting(n, ballots)

