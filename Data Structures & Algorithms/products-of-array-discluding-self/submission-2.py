class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1] * len(nums)
        suffix[len(nums)-1] = 1
        res = []

        preProd = 1
        sufProd = 1

        for i in range(1,len(nums)):
            preProd *= nums[i-1]
            prefix.append(preProd)
        
        for i in range(len(nums)-2, -1, -1):
            sufProd *= nums[i+1]
            suffix[i] = sufProd
        
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        
        return res
        

             