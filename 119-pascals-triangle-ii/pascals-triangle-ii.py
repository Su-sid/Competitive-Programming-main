class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        row = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            print(f'row for {i} is {row}')
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
              
        return row

        
        
        