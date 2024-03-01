## input
# 3
# [[0,1],[1,2],[2,0]]
# 0
# 2
# 6
# [[0,1],[0,2],[2,3],[3,5],[5,4],[4,3]]
# 0
# 5
# 6
# [[0,1],[0,2],[3,5],[5,4],[4,3]]
# 0
# 5
class Solution:
    def bfs(self, adjList, s, d):
        queue = [s]
        visited = []
        while(queue):
            item = queue.pop(0)
            if item in visited:
                continue
            if item == d :
                return True
            queue = queue + adjList[item]
            if item not in visited:
                visited.append(item)
        return False
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = {}
        for edge in edges:
            if [source, destination] == edge or edge == [destination, source]:
                return True
            if edge[0] not in adjList.keys():
                adjList[edge[0]] = [edge[1]]
            else:
                adjList[edge[0]].append(edge[1])
            if edge[1] not in adjList.keys():
                adjList[edge[1]] = [edge[0]]
            else:
                adjList[edge[1]].append(edge[0])
        return self.bfs(adjList, source, destination)