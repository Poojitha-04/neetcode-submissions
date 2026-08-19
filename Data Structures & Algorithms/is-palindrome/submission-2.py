class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2=''.join(filter(str.isalnum,s))
        s3=s2[::-1]
        
        if s3.upper()==s2.upper():
            return True
        else:
            return False
        

     
       

        