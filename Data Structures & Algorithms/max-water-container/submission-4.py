class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxcap=0
        l,r=0,len(heights)-1
        while l<r:
            prod=min(heights[l],heights[r])*(r-l)
            maxcap=max(maxcap,prod)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return maxcap

       
