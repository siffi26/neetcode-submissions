class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        hmap1 = {}
        for c in ransomNote:
            hmap1[c] = 1+hmap1.get(c, 0)
        
        hmap2 = {}
        for c in magazine:
            hmap2[c] = 1+hmap2.get(c, 0)

        for key, value in hmap1.items():
            if key not in hmap2 or hmap2[key] < value:
                return False

        return True

        