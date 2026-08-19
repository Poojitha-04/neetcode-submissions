class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        para={"}":"{","]":"[",")":"("}
        for i in s:
            if i in para:
               top=stack.pop() if stack else "#"
               if top!=para[i]:
                return False
            else:
                stack.append(i)
        return not stack
        