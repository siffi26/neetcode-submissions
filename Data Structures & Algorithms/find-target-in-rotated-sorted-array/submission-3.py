class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = int((l+r)/2)
            if nums[mid] == target:
                return mid
            
            # LEFT half is sorted
            if nums[mid]>=nums[l]:

                # is target inside sorted left half
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            
            # RIGHT half is sorted  
            else:
                # is target inside sorted right half
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1

        return -1

            



            



        