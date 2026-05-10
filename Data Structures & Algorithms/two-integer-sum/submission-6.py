class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i,n in enumerate(nums):
            remaining = target - n
            if(remaining in myMap):
                return [myMap[remaining],i]
            myMap[n] = i
        return [-1,-1]
            
