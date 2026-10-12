class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROW = len(matrix)
        COL = len(matrix[0])
        rrow = [False]*ROW
        ccol = [False]*COL
        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == 0:
                    rrow[i] = True
                    ccol[j] = True
        for r in range(ROW):
            if rrow[r]:
                for j in range(COL):
                    matrix[r][j] = 0
        for c in range(COL):
            if ccol[c]:
                for r in range(ROW):
                    matrix[r][c] = 0
            



















        # rLen = len(matrix)
        # cLen = len(matrix[0])
        # rows = [False]*rLen
        # cols = [False]*cLen
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if(matrix[i][j] == 0):
        #             rows[i] = True
        #             cols[j] = True
        # for i, r in enumerate(rows):
        #     if r:
        #         for c in range(cLen):
        #             matrix[i][c] = 0
        # for j, c in enumerate(cols):
        #     if c:
        #         for r in range(rLen):
        #             matrix[r][j] = 0

        
        
        