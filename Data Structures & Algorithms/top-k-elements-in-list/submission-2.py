class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        for n in nums:
            myMap[n] = myMap.get(n,0)+1
        heap = [(-v,k) for k,v in myMap.items()]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            popped = heapq.heappop(heap)
            res.append(popped[1])
        return res