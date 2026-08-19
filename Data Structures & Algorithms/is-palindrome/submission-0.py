class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        s_new=re.sub(r'[^a-zA-Z0-9]', '', s)
        s_new=s_new.lower()
        print(s_new)
        reverse=s_new[::-1]
        print(reverse)
        if s_new==reverse:
            return True
        else:
            return False
      

        