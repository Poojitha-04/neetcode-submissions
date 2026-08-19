class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax,rightmax=[0]*len(height),[0]*len(height)
        trap=0
        n=len(height)
        leftmax[0]=height[0]
        for i in range(1,len(height)):
            leftmax[i]=max(leftmax[i-1],height[i])
        rightmax[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],height[i])
        for i in range(len(height)):
            trap+=min(leftmax[i],rightmax[i])-height[i]
        print(leftmax,rightmax)
        return trap


            


        