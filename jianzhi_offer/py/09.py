class CQueue(object):

    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.A.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.B: return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()