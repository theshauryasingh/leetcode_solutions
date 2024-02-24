class MyCalendarThree:

    def __init__(self):
        self.k = -1
        self.intervals = []
        self.range = {}

    def book(self, startTime: int, endTime: int) -> int:
        if startTime not in self.intervals:
            heapq.heappush(self.intervals, startTime)
        if endTime not in self.intervals:
            heapq.heappush(self.intervals, endTime)
        if startTime not in self.range.keys():
            self.range[startTime] = 1
        else:
            self.range[startTime] += 1
        if endTime not in self.range.keys():
            self.range[endTime] = -1
        else:
            self.range[endTime] -= 1
        self.calculateK()
        # print(self.range, ' ------ ', self.k)
        return self.k
    
    def calculateK(self):
        if len(self.intervals) == 1:
            self.k = 1
        else:
            max = 1
            count = 0
            temp = []
            while(len(self.intervals)>0):
                item = heapq.heappop(self.intervals)
                count += self.range[item]
                # print(item, " >>> ", count)
                if count > max:
                    max = count
                temp.append(item)
            self.k = max
            self.intervals = temp
            heapq.heapify(self.intervals)

## failed attempt
## optimizing brute force by using heap
## 
## 
# class MyCalendarThree:
#     def __init__(self):
#         self.k = -1
#         self.intervals = []
#         self.range = {}

#     def book(self, startTime: int, endTime: int) -> int:
#         if startTime not in self.intervals:
#             heapq.heappush(self.intervals, startTime)
#         if endTime not in self.intervals:
#             heapq.heappush(self.intervals, endTime)
#         if startTime not in self.range.keys():
#             self.range[startTime] = [True, 1]
#         else:
#             self.range[startTime][1] += 1
#         if endTime not in self.range.keys():
#             self.range[endTime] = [False, 0]
#         else:
#             self.range[endTime][0] = False
#         self.calculateK()
#         print('---------------', self.intervals, '---------------', self.k)
#         return self.k
    
#     def calculateK(self):
#         if len(self.intervals) < 2:
#             self.k = 0
#         else:
#             max = 1
#             current = 0
#             temp = []
#             while(len(self.intervals)>0):
#                 item = heapq.heappop(self.intervals)
#                 print(item, " >>", self.intervals, "<<")
#                 if self.range[item][0] == False:
#                     if current > max:
#                         max = current
#                     current = 0
#                     print(item, current)
#                 current += self.range[item][1]
#                 print(item, current)
#                 temp.append(item)
#             self.k = max
#             self.intervals = temp
#             heapq.heapify(self.intervals)
            

##
## brute force
##
## input:
# ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
# [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
#
# class MyCalendarThree:

#     def __init__(self):
#         self.k = -1
#         self.intervals = []
#         self.range = {}

#     def book(self, startTime: int, endTime: int) -> int:
#         self.intervals.append([startTime, endTime])
#         print(self.range)
#         for i in range(startTime, endTime):
#             if i not in self.range.keys():
#                 self.range[i] = 1
#             else:
#                 self.range[i] += 1
#         self.calculateK()
#         return self.k
    
#     def calculateK(self):
#         if len(self.intervals) == 1:
#             self.k = 1
#         else:
#             max = 1
#             for k,v in self.range.items():
#                 if v > max:
#                     max = v
#             self.k = max
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)