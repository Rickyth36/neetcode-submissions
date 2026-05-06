class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)):
            ref = nums[i]
            for j in range(i+1,len(nums)):
                if ref == nums[j]:
                    return True
            
        return False