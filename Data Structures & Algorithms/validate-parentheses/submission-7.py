class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in '{([':
                stack.append(s[i])
                print(stack)
            elif stack:
                if (s[i] == ']' and stack[-1] == '[') or \
                   (s[i] == '}' and stack[-1] == '{') or \
                   (s[i] == ')' and stack[-1] == '('):
                    stack.pop(-1)
                else:
                    return False
            else:
                return False
        if not stack:
            return True
        else:
            return False




    