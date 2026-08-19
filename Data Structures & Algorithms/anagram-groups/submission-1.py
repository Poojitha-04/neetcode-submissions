class Solution:
   
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string=defaultdict(list)
        for s in strs:
            anagram=''.join(sorted(s))
            string[anagram].append(s)
        return list(string.values())
       
        
        