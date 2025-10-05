class Solution {

    public static int rec(int idx, int[] coins, int amount,int[][]dp){
        if(idx<0){
            return (int)1e9;
        }
        if(amount == 0){
            return 0;
        }
        if(amount < 0){
            return (int)1e9;
        }
        if(amount == coins[idx]){
            return 1;
        }
        if(dp[idx][amount] != -1) return dp[idx][amount];
        int take = (int)1e9;
        if(amount - coins[idx] >= 0)
            take = rec(idx,coins,amount-coins[idx],dp) + 1;
        int notTake = rec(idx-1,coins,amount,dp);
        dp[idx][amount] = Math.min(take,notTake);
        return Math.min(take,notTake);
    }

    public int coinChange(int[] coins, int amount) {
        Arrays.sort(coins);
        int[][] dp = new int[coins.length][amount+1];
        for (int[] row : dp) Arrays.fill(row, -1);
        int ans = rec(coins.length-1,coins,amount,dp);
        if(ans == (int)1e9) return -1;
        return ans;

    }
}