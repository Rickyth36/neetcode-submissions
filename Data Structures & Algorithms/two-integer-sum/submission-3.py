class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(0,len(nums)):
            remaining = target - nums[i]
            if remaining in hashMap.keys():
                return [hashMap.get(remaining),i]
            hashMap[nums[i]] = i
        return [-1,-1]