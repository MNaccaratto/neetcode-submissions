class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        open_brackets = ["(","[","{"]
        close_brackets = [")","]","}"]

        prev = ""

        if len(s) == 1:
            return False

        for i in range(len(s)):
            if s[i] in open_brackets:
                prev = s[i]
                stack.append(s[i])
                
            elif s[i] in close_brackets:
                
                if len(stack) == 0:
                    return False

                if s[i] == ")" and prev == "(":
                    stack.pop()
                elif s[i] == "}" and prev == "{":
                    stack.pop()
                elif s[i] == "]" and prev == "[":
                    stack.pop()
                else:
                    return False
                
                if len(stack) > 0:
                    prev = stack[-1]

                
            
        if len(stack) == 0:
            return True
        return False