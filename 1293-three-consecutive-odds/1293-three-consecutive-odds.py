class Solution:
    def threeConsecutiveOdds(self, arr):
        n = len(arr)
        if n < 3:
            return False
        
        i = 0
        while i <= n - 3:
            if arr[i + 2] % 2 == 0:
                i += 3
            elif arr[i + 1] % 2 == 0:
                i += 2
            elif arr[i] % 2 == 0:
                i += 1
            else:
                return True
        return False