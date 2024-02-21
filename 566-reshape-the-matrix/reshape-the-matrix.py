class Solution:
    def isValid(self, r1, c1, r, c):
        if r1*c1 == r*c:
            return True
        return False
        
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        r1 = len(mat)
        c1 = len(mat[0])
        if not self.isValid(r1, c1, r, c):
            return mat
        flatMat = []
        for i in range(r1):
            for j in range(c1):
                flatMat.append(mat[i][j])
        print(flatMat)
        newMat = []
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(flatMat.pop(0))
                # temp.append(flatMat[i+j])
            newMat.append(temp)
        return newMat
        
        
        