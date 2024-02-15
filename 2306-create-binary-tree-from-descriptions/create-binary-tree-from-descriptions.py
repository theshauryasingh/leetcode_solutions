# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        db = {}
        for i in descriptions:
            if i[0] not in db.keys():
                a = TreeNode(i[0])
                db[i[0]] = [False, a]
            else:
                a = db[i[0]][1]
            if i[1] not in db.keys():
                b = TreeNode(i[1])
                db[i[1]] = [True,b]
            else:
                b = db[i[1]][1]
                db[i[1]][0] = True
            if i[2] == 1:
                a.left = b
            else:
                a.right = b
        # print(db)
        for key,val in db.items():
            if val[0] == False:
                return val[1] 