class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rLen = len(matrix)
        cLen = len(matrix[0])
        row = [False]*rLen
        col = [False]*cLen
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        for i, r in enumerate(row):
            if r:
                for c in range(cLen):
                    matrix[i][c] = 0
        for j, c in enumerate(col):
            if c:
                for r in range(rLen):
                    matrix[r][j] = 0

















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

        
        
        