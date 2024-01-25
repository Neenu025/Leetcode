class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        for word in words:
            split_word = word.split(separator)
            for sub_word in split_word:
                if sub_word != "":
                    result.append(sub_word)

        result = []
        return result

[
