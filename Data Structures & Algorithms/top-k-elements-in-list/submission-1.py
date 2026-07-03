class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []

        countNums = {}
        
        for i, num in enumerate(nums):
            if nums[i] not in countNums:
                countNums[nums[i]]=1
            else:
                countNums[nums[i]]+=1
        sorted_Counts = dict(sorted(countNums.items(), key=lambda item: item[1], reverse=True))
        l = 1
        res = []
        print(sorted_Counts)
        for key, value in sorted_Counts.items():
            if l>k:
                break
            else:
                res.append(key)
                l+=1
        return res

