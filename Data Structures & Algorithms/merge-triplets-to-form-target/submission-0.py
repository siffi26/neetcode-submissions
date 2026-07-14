class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # check for a <= target[0], b <= target[1], c <= target[2]
        matched = [False, False, False]

        for each in triplets:
            # if any value is greater than target's
            if each[0]>target[0] or each[1]>target[1] or each[2]>target[2]:
                continue
            
            if each[0] == target[0]:
                matched[0] = True
            if each[1] == target[1]:
                matched[1] = True
            if each[2] == target[2]:
                matched[2] = True

        if matched[0] == True and matched[1] == True and matched[2] == True:
            return True
        else:
            return False
