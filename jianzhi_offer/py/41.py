import heapq


class MedianFinder:

    def __init__(self):
        # 当前大顶堆和小顶堆的元素个数之和
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        self.count += 1
        # 因为 Python 中的堆默认是小顶堆，所以要传入一个 tuple，用于比较的元素需是相反数，
        # 才能模拟出大顶堆的效果
        if len(self.max_heap) == 0:
            heapq.heappush(self.max_heap, (-num, num))

        elif num <= self.max_heap[0][1]:
            heapq.heappush(self.max_heap, (-num, num))
            while len(self.max_heap) > len(self.min_heap)+1:
                _, max_heap_top = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, max_heap_top)
        else:
            heapq.heappush(self.min_heap, num)
            while len(self.max_heap) < len(self.min_heap):
                min_heap_top = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, (-min_heap_top, min_heap_top))

    def findMedian(self):
        if self.count & 1:
            # 如果两个堆合起来的元素个数是奇数，数据流的中位数大顶堆的堆顶元素
            return self.max_heap[0][1]
        else:
            # 如果两个堆合起来的元素个数是偶数，数据流的中位数就是各自堆顶元素的平均值
            return (self.min_heap[0] + self.max_heap[0][1]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()