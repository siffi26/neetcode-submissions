class Solution:
    def isPalindrome(self, s: str) -> bool:
        orig = s.replace(" ", "").lower()
        cleaned_orig = "".join([char for char in orig if char.isalnum()])

        r = s[::-1]
        rev = r.replace(" ", "").lower()
        cleaned_rev = "".join([char for char in rev if char.isalnum()])

        print(cleaned_rev)
        print(cleaned_orig)
        if cleaned_rev == cleaned_orig:
            return True
        else:
            return False
        