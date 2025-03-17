class Solution {
    public int searchInsert(int[] nums, int target) {
    int l = 0;
        int r = nums.length - 1;
        int mid = l + (r-l)/2;
        while(l<=r){
            mid = l + (r-l)/2;
            if(nums[mid] == target){
                System.out.println(mid);
                return mid;
            }
            if(nums[mid] > target){
                System.out.println(mid);
                r = mid-1;
            }
            else{
                System.out.println(mid);
                l = mid+1;
            }
        }
        
        if(target > nums[mid]) return mid+1;
        return mid;
    }
}