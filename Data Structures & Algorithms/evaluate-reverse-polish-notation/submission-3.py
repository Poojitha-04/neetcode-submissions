import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
        for i in range(len(tokens)):
            if tokens[i].lstrip('-').isdigit():
               # print(tokens[i],i)
                stack.append(tokens[i])
            else:
                val1=stack.pop()
                #print(val1)
                val2=stack.pop()
                op=ops.get(tokens[i])
                res=(op(int(val2),int(val1)))
                print(res,"result")
                stack.append(res)
        return int(stack[0])
                


            

            
            

            

        
        