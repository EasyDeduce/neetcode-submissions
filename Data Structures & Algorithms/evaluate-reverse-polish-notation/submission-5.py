class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def isinteger(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
        for token in tokens:
            if isinteger(token):
                stack.append(int(token))
            else:
                op2= stack.pop()
                op1= stack.pop()
                if token=="+":
                    stack.append(op2+op1)
                elif token=="-":
                    stack.append(op1-op2)
                elif token=="*":
                    stack.append(op2*op1)
                elif token=="/":
                    stack.append(int(op1/op2))
            # print(stack)
        return stack.pop() 