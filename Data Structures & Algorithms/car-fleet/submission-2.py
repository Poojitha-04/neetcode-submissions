class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed),reverse=True)
        times=[(target-p)/s for p,s in cars]
        fleet,prev=0,0
        for t in times:
            if t>prev:
                fleet+=1
                prev=t
        return fleet


        
        

        
