class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # trips = [[2,1,5],[3,3,7]], capacity = 4
        trips2 = []
        for passenger, st, end in trips:
            trips2.append([st, passenger])
            trips2.append([end, -1 * passenger])
        trips2.sort() #key=lambda x: (x[0], x[1])
        currPassengers = 0
        # print(trips2)
        for location, passenger in trips2:
            currPassengers += passenger
            # print(currPassengers)
            if currPassengers > capacity or currPassengers < 0:
                return False
        return True

# approach II to rewrite trips list 
        # trips2 = []
        # for passenger, st, end in trips:
        #     trips2.append([st, passenger, True])
        #     trips2.append([end, passenger, False])
        # trips2.sort(key=lambda x: (x[0], x[2]))
        # currPassengers = 0
        # # print(trips2)
        # for location, passenger, status in trips2:
        #     if status:
        #         currPassengers += passenger
        #     else:
        #         currPassengers -= passenger
        #     # print(currPassengers)
        #     if currPassengers > capacity or currPassengers < 0:
        #         return False
        # return True
    
    
    
# approaching problem by keeping two pointers one to track distance and another to track passenger        
#         i = 0
#         j = trips[0][]
#         while(i<len(trips)):
#             if curCapacity > capacity:
#                 return False
            
#             i += 1
#         return True