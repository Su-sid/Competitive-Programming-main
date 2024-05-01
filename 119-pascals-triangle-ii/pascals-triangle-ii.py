class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        # row = [1] * (rowIndex + 1)
        # for i in range(1, rowIndex):
        #     print(f'row for {i} is {row}')
        #     for j in range(i, 0, -1):
        #         row[j] += row[j - 1]
              
        # return row

        if rowIndex == 0:
            return [1] 
        prev = self.getRow(rowIndex-1)
        row = [1]

        for i in range(1, len(prev)):
            row.append(prev[i-1] + prev[i])

        row.append(1)
        return row        
