class Solution:
    def isValid(self, s: str) -> bool:
        #we use a stack to solve this problem 
        #our strategy will go something like this 
        #we'll iterate from start to finish on the string 
        #adding the char to the stack as we go through it
        #if the previous char(i.e the stack's top element is the corresponding closed bracket then we remove it from the list)
        #if the stack is empty at the end then we know it's valid else not
        stack = []
        #the important thing to note here is that we have to know that anytime the top of the stack 
        #contains a closing bracket, this automatically implys a invalid string, which informs our mapping
        mapping = {
            '}': '{',
            ')': '(',
            ']': '[',
            }
        for char in s:
            if stack:
                if char in mapping and stack[-1] == mapping[char]:
                    stack.pop(-1)
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return len(stack) == 0 
