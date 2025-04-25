class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return s
            
        rows = [''] * numRows
        current_row = 0
        step = 1
        
        for char in s:
            rows[current_row] += char
            
            if current_row == 0:
                step = 1
            elif current_row == numRows - 1:
                step = -1
                
            current_row += step
            
        return ''.join(rows)