class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROW = [False]*len(matrix)
        COL = [False]*len(matrix[0])
        ROWLen = len(matrix)
        COLLen = len(matrix[0])
        for i in range(ROWLen):
            for j in range(COLLen):
                if matrix[i][j] == 0:
                    ROW[i] = True
                    COL[j] = True
        for i in range(ROWLen):
            if ROW[i]:
                for j in range(COLLen):
                    matrix[i][j] = 0
        for j in range(COLLen):
            if COL[j]:
                for i in range(ROWLen):
                    matrix[i][j] = 0

            



















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

        
        
        