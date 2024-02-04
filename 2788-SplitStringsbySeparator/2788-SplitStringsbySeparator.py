class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            split_word = word.split(separator)
            print(split_word)
            for sub_word in split_word:
                if sub_word != "":
                    result.append(sub_word)
        return result



        
[
