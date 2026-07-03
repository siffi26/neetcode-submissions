class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if sorted(s) != sorted(t):
            return False
        else:
            return True
        # counts_s = {}
        # counts_t = {}
        # for i in s:
        #     if i in counts_s:
        #         counts_s[i] += 1
        #     else:
        #         counts_s[i] = 1

        # for j in t:
        #     if j in counts_t:
        #         counts_t[j] += 1
        #     else:
        #         counts_t[j] = 1

        # print(counts_t)
        # print(counts_s)
        # for key, value in counts_s.items():
        #     print(key)
        #     if key in counts_s and key in counts_t:
        #         if counts_s[key] != counts_t[key]:
        #             return False
        #         else:
        #             continue
        #     else:
        #         return False
        # return True