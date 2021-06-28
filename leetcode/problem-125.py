class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.method1(s)


    def method1(self, s: str) -> bool:
        s = s.lower()

        left, right = 0, len(s)-1
        while left < right:
            while left < right and not str.isalnum(s[left]):
                left += 1
            while left < right and not str.isalnum(s[right]):  
                right -= 1

            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1

        return True
