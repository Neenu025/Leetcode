class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
            return False
        if len(s) != len(goal):
        
        if s == goal:
            # If s and goal are the same, check if s contains duplicate characters
            return len(set(s)) < len(s)
        
        # Find the positions where the characters differ
        diffs = [(a, b) for a, b in zip(s, goal) if a != b]
        
        # There should be exactly two differences, and they should be reversible
        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]

"
