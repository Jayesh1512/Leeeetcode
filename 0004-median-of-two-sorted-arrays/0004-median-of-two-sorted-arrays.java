import java.util.Arrays;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] arr = new int[nums1.length + nums2.length];
        int m = nums1.length;
        int n = nums2.length;
        int k = 0;
        
        for (int i = 0; i < nums1.length; i++) {
            arr[k++] = nums1[i];
        }
        for (int i = 0; i < nums2.length; i++) {
            arr[k++] = nums2[i];
        }
        
        Arrays.sort(arr);
        
        if ((m + n) % 2 == 0) {
            int less = (m + n) / 2 - 1;
            int more = (m + n) / 2;
            System.out.println(less);
            System.out.println(more);
            double ans = (arr[less] + arr[more]) / 2.0;
            return ans;
        } else {
            int mid = (m + n) / 2;
            return arr[mid];
        }
    }
}
