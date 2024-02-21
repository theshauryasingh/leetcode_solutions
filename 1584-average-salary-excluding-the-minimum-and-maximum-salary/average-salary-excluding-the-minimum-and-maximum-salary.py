class Solution:
    def average(self, salary: List[int]) -> float:
        #second approach, optimizing total count
        minSal = float(inf)
        maxSal = float(-inf)
        totalSal = 0
        for singleSalary in salary:
            if singleSalary < minSal:
                minSal = singleSalary
            if singleSalary > maxSal:
                maxSal = singleSalary
            totalSal += singleSalary
        totalSal -= minSal
        totalSal -= maxSal
        return totalSal/(len(salary)-2)        
        
        
        
        #first approach
        # minSal = float(inf)
        # maxSal = float(-inf)
        # totalSal = 0
        # count = 0
        # for singleSalary in salary:
        #     if singleSalary < minSal:
        #         minSal = singleSalary
        #     if singleSalary > maxSal:
        #         maxSal = singleSalary
        #     totalSal += singleSalary
        #     count +=1
        #     # print(minSal, maxSal, totalSal, count)
        # totalSal -= minSal
        # totalSal -= maxSal
        # return totalSal/(count-2)
            