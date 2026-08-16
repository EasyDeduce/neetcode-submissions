class MedianFinder:

    def __init__(self):
        self.L = []
    def addNum(self, num: int) -> None:
        self.L.append(num)
        self.L.sort()

    def findMedian(self) -> float:
        if len(self.L) % 2 == 0:
            mid = len(self.L) // 2
            return float((self.L[mid] + self.L[mid - 1]) / 2)
        else:
            mid = len(self.L) // 2
            return float(self.L[mid])