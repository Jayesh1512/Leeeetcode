class Solution {
public:
    int uniquePaths(int m, int n) {
        // if(i==0 && j==0){
        //     return 1;
        // }

        // int left = 0, right = 0;
        // if(i>0){
        //     left = f(i - 1, j)
        // }
        // if(j>0){
        //     right = f(i, j-1)
        // }

        // return left + right;

        vector<vector<int>> dp(m, vector<int> (n, 0));
        
        for(int i = 0; i <m; i++){
            for(int j= 0; j<n; j++){
                if(i == 0 && j == 0) dp[0][0] = 1;
                else{

                    int left = 0, up = 0;
                    if(i > 0){
                        left = dp[i -1][j];
                    }
                    if(j> 0){
                        up = dp[i][j-1];
                    }
                    dp[i][j] = left + up;
                }
            }
        }

        return dp[m -1][n -1];

        
    }
};