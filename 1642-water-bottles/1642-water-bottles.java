class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int ans = numBottles;
        int remBottles = numBottles;

        while(remBottles >= numExchange){
            int newBottles = remBottles / numExchange; 
            ans += newBottles;
            remBottles = remBottles % numExchange + newBottles; 
        }
        return ans;
    }
}