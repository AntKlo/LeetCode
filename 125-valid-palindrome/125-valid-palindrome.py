class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.lower()
        s = s.replace(' ', '')
        return s == s[::-1]