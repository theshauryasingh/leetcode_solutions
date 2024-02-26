class Solution:
    def bfs(self, root, adjList):
        visited = [root]
        queue = [root]
        while(len(queue)!=0):
            node = queue.pop(0)
            if node in adjList.keys():
                queue = queue + adjList[node]
            if node not in visited:
                visited.append(node)
        print(visited)
        return len(visited)
    
    def dfs(self, root, adjList):
        visited = [root]
        stack = [root]
        while(len(stack)!=0):
            node = stack.pop()
            if node in adjList.keys():
                stack = stack + adjList[node]
            if node not in visited:
                visited.append(node)
        return len(visited)
    
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # preorder given
        # create child to parent hashmap(single parent)
        # find root(single root)
        # check dfs(connected graph)
        childParent ={}
        adjList ={}
        for i in range(n):
            node = leftChild[i]
            if node != -1:
                if node in childParent.keys():
                    return False
                childParent[node] = i
                if i not in adjList.keys():
                    adjList[i] = [node]
                else:
                     adjList[i].append(node)
            node =  rightChild[i]
            if node != -1:
                if node in childParent.keys():
                    return False
                childParent[node] = i
                if i not in adjList.keys():
                    adjList[i] = [node]
                else:
                     adjList[i].append(node)
        root = -1
        for i in range(n):
            if childParent.get(i, None) == None:
                if root > -1:
                    return False
                root = i
        if root == -1:
            return False
        if n != self.bfs(root, adjList):
            return False
        # if n != self.dfs(root, adjList):
        #     return False
        print(n, root, childParent, adjList)
        
        
        return True