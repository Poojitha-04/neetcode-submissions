class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_cap=0
        i,j=0,len(heights)-1
        while i<j:
            cap=min(heights[i],heights[j])*(j-i)
            max_cap=max(max_cap,cap)
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return max_cap

