class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer = []
        pointer = 0
        for i in range(1,n+1):
            answer.append('Push')
            if target[pointer] == i:
                pointer +=1
            else:
                answer.append('Pop')
            if pointer == len(target):
                break
        return answer