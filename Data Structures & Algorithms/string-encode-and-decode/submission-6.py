class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}:{s}")
        return "".join(res) 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Step 1: Read the full number (length) until ':'
            j = i
            while s[j] != ':':
                j += 1
            length = int(s[i:j])
            
            # Step 2: Extract the string of `length` characters
            j += 1  # move past ':'
            res.append(s[j:j+length])
            
            # Step 3: Move to next encoded part
            i = j + length
        return res



        
        