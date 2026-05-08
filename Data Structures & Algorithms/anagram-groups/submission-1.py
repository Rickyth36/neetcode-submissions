class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)

            if key not in myMap:
                myMap[key] = []
            myMap[key].append(s)
        
        return list(myMap.values())

