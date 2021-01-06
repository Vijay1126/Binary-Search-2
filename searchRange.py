class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        found = False
        def binaryLeft(target):
            left = 0
            right = len(nums)-1
            
            while left<=right:
                mid = left+(right-left)//2
                value = nums[mid]
                if (mid == left and value==target) or (value==target and nums[mid-1]!=target):
                    return mid
                elif value < target:
                    left = mid+1
                else:
                    right = mid-1
            return -1
        def binaryRight(target):
            left = 0
            right = len(nums)-1
            
            while left<=right:
                mid = left+(right-left)//2
                value = nums[mid]
                if (mid == right and value==target) or (value==target and nums[mid+1]!=target):
                    return mid
                elif value <= target:
                    left = mid+1
                else:
                    right = mid-1
            return -1
    
      
        left = binaryLeft(target)
        right = binaryRight(target)

        return [left, right]

                    
Time : log(n)
Space: O(1)
