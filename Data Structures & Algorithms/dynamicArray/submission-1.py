class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0.")
        self.arr = [0] * capacity  # Pre-allocate with default values
        self.length = 0            # Current number of elements
        self.capacity = capacity   # Total capacity



    def get(self, i: int) -> int:
        return self.arr[i]



    def set(self, i: int, n: int) -> None:
        self.arr[i]=n


    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length]=n
        self.length += 1



    def popback(self) -> int:
        if self.length == 0:
            raise IndexError("Pop from empty array.")
        self.length -= 1
        return self.arr[self.length]
    
 

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_arr = [0] * new_capacity
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity



    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
