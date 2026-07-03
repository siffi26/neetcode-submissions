class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0] or target > nums[-1]:
            return -1
        
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = int((l+r)/2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid+1
            elif target < nums[mid]:
                r = mid-1
        return -1

        