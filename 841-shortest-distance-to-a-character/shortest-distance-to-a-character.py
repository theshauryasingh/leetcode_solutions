class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        leftArr  = [] # [-1] * (len(s)-1)
        rightArr = [] # [-1] * (len(s)-1)
        answer   = []
        maxN = float(inf)
        recent = -1
        for letter in s:
            if letter == c:
                recent = 0
                leftArr.append(recent)
            elif recent == -1:
                leftArr.append(maxN)
            else:
                recent +=1
                leftArr.append(recent)
        recent = -1
        for letter in s[::-1]:
            if letter == c:
                recent = 0
                rightArr = [recent] + rightArr
            elif recent == -1:
                rightArr = [maxN] + rightArr
            else:
                recent +=1
                rightArr = [recent] + rightArr
        print(leftArr, rightArr)
        for i in range(len(leftArr)):
            answer.append(min(leftArr[i], rightArr[i]))
        return answer