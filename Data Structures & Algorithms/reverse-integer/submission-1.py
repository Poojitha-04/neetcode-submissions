class Solution:
    def reverse(self, x: int) -> int:
        maxint,minint=(2**31)-1,-2**31
        sign=1
        if x<0:
            sign=-1
            x=x*-1
        res=0
        while x!=0:
            digit=x%10
            res=res*10+digit
            x=x//10
        res=res*sign
        if res>maxint or res<minint:
            return 0
        else:
            return res

