class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        adjList = {}
        for trust_rel in trust:
            if trust_rel[1] not in adjList.keys():
                adjList[trust_rel[1]] = [trust_rel[0]]
            else:
                adjList[trust_rel[1]].append(trust_rel[0])
        judge_candidates = {}
        for node, trust_rel in adjList.items():
            if len(trust_rel) == n-1 :
                judge_candidates[node] = True
        for candidate,status in judge_candidates.items():
            for trust_rel in trust:
                if trust_rel[0] == candidate:
                    judge_candidates[candidate] = False
        for candidate,status in judge_candidates.items():
            if status == True:
                return candidate
        return -1