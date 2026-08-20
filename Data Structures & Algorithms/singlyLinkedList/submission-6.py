class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def get(self, index: int) -> int:
        count=0
        curr=self.head
        while curr:
            if count == index:
                return curr.val
            count+=1
            curr=curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=Node(val)

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        curr=self.head
        count=0
        prev=None
        while curr and count != index:
            count+=1
            prev=curr
            curr=curr.next
        if not curr:
            return False
        prev.next=curr.next
        return True
        
    def getValues(self) -> List[int]:
        curr=self.head
        res=[]
        while curr!=None:
            res.append(curr.val)
            curr=curr.next
        return res
