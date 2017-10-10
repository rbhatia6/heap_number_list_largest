import heapq

class heapLargest:
    cnt = 0
    numLst = [2,6,1,7,3,8,5,2,0,9]

    def __init__(self, cnt):
        self.cnt = cnt

    def heapNum(self, x): 
        heapq.heapify(self.numLst)
        if len(self.numLst) > self.cnt:
            heapq.heappushpop(self.numLst, x)
        else:
            heapq.heappush(self.numLst, x)
        return heapq.nlargest(self.cnt, self.numLst)

if __name__ == "__main__":
    heapl = heapLargest(5)
    print(heapl.heapNum(13))
