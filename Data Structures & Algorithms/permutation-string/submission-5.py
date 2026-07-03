class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        u_s1 = sorted(s1)
        l_s1 = len(s1)

        r = len(s2)- l_s1 + 1
        for i in range(r):
            end = i + l_s1
            subseq = sorted(s2[i: end])
            # print(subseq, " || ", u_s1)
            if u_s1 == subseq:
                return True
        return False



        