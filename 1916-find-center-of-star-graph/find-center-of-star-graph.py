class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjList = {}
        for edge in edges:
            if edge[0] not in adjList.keys():
                adjList[edge[0]] = [edge[1]]
            else:
                adjList[edge[0]].append(edge[1])
            if edge[1] not in adjList.keys():
                adjList[edge[1]] = [edge[0]]
            else:
                adjList[edge[1]].append(edge[0])
        for k,v in adjList.items():
            if len(v) == len(edges):# len(adjList)-1:
                return k