class Solution(object):
    def partition(self, s):
        self.result=[]
        def helper(i,arr):

            if i==len(s):

                self.result.append(list(arr))
                return

            
            for j in range(i+1,len(s)+1):

                if s[i:j]==s[i:j][::-1] and len(s[i:j])>=1:

                    arr.append(s[i:j])
                    helper(j,arr)
                    arr.pop()

        helper(0,[])
        return self.result

        