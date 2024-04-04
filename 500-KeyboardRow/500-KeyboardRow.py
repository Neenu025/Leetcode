            unique = set(word.lower())
        for word in words:
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output = []
        first_row =  set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")

            if unique <= first_row or unique <= second_row or unique <= third_row:
                output.append(word) 
        return output
[
