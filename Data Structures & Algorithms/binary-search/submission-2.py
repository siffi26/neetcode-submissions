class Solution:
    def search(self, nums: List[int], target:int) -> int:

        def binary_search(l:int, r:int, nums:List[int], target:int) -> int:
            
            while l<=r:
                mid = int((l+r)/2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid-1
                elif nums[mid] < target:
                    l = mid+1

            return -1

        i = 0
        j = len(nums)-1
        return binary_search(i, j, nums, target)


