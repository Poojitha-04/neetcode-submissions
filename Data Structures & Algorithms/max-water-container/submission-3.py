class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_cap=0
        l,r=0,len(heights)-1
        while l<r:
            prod=min(heights[l],heights[r])*(r-l)
            max_cap=max(max_cap,prod)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return max_cap
