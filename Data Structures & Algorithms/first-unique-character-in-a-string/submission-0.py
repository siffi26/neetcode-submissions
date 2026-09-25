class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = {}

        for c in s:
            hmap[c] = 1+ hmap.get(c, 0)

        for i, c in enumerate(s):
            if hmap[c]==1:
                return i
        return -1
        