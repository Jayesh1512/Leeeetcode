class Solution {
    public int[] searchRange(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        int[] result = new int[]{-1, -1};
        
        while (l <= r) {
            int mid = (l + r) / 2;

            if (nums[mid] < target) {
                l = mid + 1;
            } else if (nums[mid] > target) {
                r = mid - 1;
            } else {
                
                int left = mid;
                int right = mid;

                while (left - 1 >= 0 && nums[left - 1] == target) {
                    left--;
                }

              
                while (right + 1 < nums.length && nums[right + 1] == target) {
                    right++;
                }

                result[0] = left;
                result[1] = right;

                return result;
            }
        }
        return result;
    }
}