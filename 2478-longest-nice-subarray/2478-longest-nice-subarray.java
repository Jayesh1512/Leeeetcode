class Solution {
    public int longestNiceSubarray(int[] nums) {
        int l = 0;
        int r = 0;
        int maxLength = 1;
        ArrayList<Integer> a = new ArrayList<>();
        
        while (r < nums.length) {
            a.add(nums[r]);
            while (!check(a)) {
                a.remove(0);
                l++;
            }
            maxLength = Math.max(maxLength, a.size());
            r++;
        }
        return maxLength;
    }

    public boolean check(ArrayList<Integer> a) {
        for (int i = 0; i < a.size(); i++) {
            for (int j = i + 1; j < a.size(); j++) { 
                if ((a.get(i) & a.get(j)) != 0) {
                    return false;
                }
            }
        }
        return true;
    }
}
