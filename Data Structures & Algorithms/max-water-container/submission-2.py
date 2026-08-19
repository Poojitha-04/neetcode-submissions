class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_cap=0
        j=len(heights)-1
        for i in range(len(heights)):
            for j in range(i,len(heights)):
                prod=min(heights[i],heights[j])*(j-i)
                print(prod)
                if max_cap<prod:
                    max_cap=prod
        return max_cap
