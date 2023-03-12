class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ct = 0
        vowels = {"a","e","i","o","u"}
        for i in words[left:right+1]:
            if i[0] in vowels and i[-1] in vowels:
                ct+=1
                
        return ct
            