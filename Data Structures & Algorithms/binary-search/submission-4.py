class Solution:
    def search(self, nums: List[int], target:int) -> int:
        def binary_search(left, right):
            while(left<=right):
                mid = int((left+right)/2)

                if nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    left = mid+1
                elif target < nums[mid]:
                    right = mid-1

            return -1

        left = 0
        right = len(nums)-1
        return binary_search(left, right)


