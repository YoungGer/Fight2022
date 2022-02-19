class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        push_id = 0
        pop_id = 0
        
        while push_id < len(pushed) or pop_id < len(popped):
            if ((not stack) or stack[-1] != popped[pop_id]) and pop_id<len(popped) and push_id<len(pushed):
                stack.append(pushed[push_id])
                push_id += 1
            elif  stack and stack[-1] == popped[pop_id]:
                stack.pop()
                pop_id += 1
            else:
                return False
            
        return push_id == len(pushed) and pop_id == len(popped) and len(stack) == 0