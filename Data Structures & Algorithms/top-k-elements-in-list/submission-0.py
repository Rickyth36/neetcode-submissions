class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            myMap = {}
            res = []
            for n in nums:
                myMap[n] = myMap.get(n,0) + 1;
            heap = [(v*-1,k) for k,v in myMap.items()]
            heapq.heapify(heap)

            for i in range(k):
                popped = heapq.heappop(heap)
                res.append(popped[1])
            return res