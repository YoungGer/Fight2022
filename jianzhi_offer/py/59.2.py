from collections import deque
class MaxQueue(object):
    def __init__(self):
        self.queue = deque([])
        self.sort_queue = deque([])

    def max_value(self):
        """
        :rtype: int
        """
        return self.sort_queue[0] if self.sort_queue else -1


    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)
        while self.sort_queue and self.sort_queue[-1] < value:
            self.sort_queue.pop()
        self.sort_queue.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.queue or not self.sort_queue:
            return -1
        
        if self.queue[0] != self.sort_queue[0]:
            return self.queue.popleft()
        else:
            self.sort_queue.popleft()
            return self.queue.popleft()


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()