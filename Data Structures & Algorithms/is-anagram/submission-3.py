class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        SHashMap = {}
        THashMap = {}
        if(len(s) != len(t)):
            return False
        for ch in s:
            SHashMap[ch] = SHashMap.get(ch,0) + 1
        for ch in t:
            THashMap[ch] = THashMap.get(ch,0) + 1
        for i in SHashMap:
            if SHashMap.get(i) != THashMap.get(i):
                return False
        return True
        