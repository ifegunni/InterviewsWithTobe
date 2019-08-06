import heapq 
#  10 2 3 4 5 11 0 3
    
# nth order stactics
# 1st smallest value is 0
# 8th largest value is 0

# 5th order =  value at index 4

#:: 1st smallest order:

"""
O(nlogn)

"""

# def OS(array, k):
    
#     min1 = 0
#     min2 = 0
#     for i in range(1, len(array)):
#         if array[i] < array[min1]:
#             min2 = min1
#             min1 = i
#         elif array[i] <array[min2]:
#             min2 = i
#     return array[min1]

from heapq import heappush, heappop
def OSHeap(array, k):
    maxHeap = createHeap(k)
    
    for i in range(0, len(array)):
        if array[i] < maxHeap.peak():
            maxHeap.remove()
            maxHeap.push(array[i])
    Kth_value = maxHeap.remove()      
    return Kth_value

"""
    3
  1   2
  
    1
  2   3 
  
  -3
-1  -2
"""
def createHeap(k):
    heap = Heap()
    for i in range(k):
        heap.push(float("inf"))
    return heap 
    
class Heap:
    def __init__(self):
        self.My_heap = []
        
    def push(self,value):
        heappush(self.My_heap, -value)
        #::heapq 
    
    def remove(self):
        return heappop(self.My_heap) * -1
    
    def peak(self):
        Value = self.My_heap[0] * -1
        return Value
    
    
    
    
    
def test1(k):
    arr = [10, 2, 3, 4, 5, 11, 0, 3]
    print(OSHeap(arr,k))
    print(sorted(arr))
    
test1(7)
