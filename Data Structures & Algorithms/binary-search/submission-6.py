class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start,end=0,len(nums)-1
        flag=0
        while start<=end:
            mid=start+((end-start)//2)
            if nums[mid]>target:
                end=mid-1
                print(mid)
            elif nums[mid]<target:
                start=mid+1
            elif nums[mid]==target:
                return mid
        return -1


            
       