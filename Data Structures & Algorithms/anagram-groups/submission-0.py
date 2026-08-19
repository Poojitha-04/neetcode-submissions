class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for s in strs:
            try:
                existing=res[''.join(sorted(s))]
                existing.append(s)
                res[''.join(sorted(s))]=existing
            except:
                res[''.join(sorted(s))]=[s]
        return(list(res.values()))
        