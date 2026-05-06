class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i,n in enumerate(nums):
            prod = 1
            for j,m in enumerate(nums):
                if j == i:
                    continue
                prod *= m
            res.append(prod)
        return res