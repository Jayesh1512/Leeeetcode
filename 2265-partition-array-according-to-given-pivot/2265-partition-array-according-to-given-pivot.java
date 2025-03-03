import java.util.*;

class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        ArrayList<Integer> less = new ArrayList<>();
        ArrayList<Integer> equal = new ArrayList<>();
        ArrayList<Integer> great = new ArrayList<>();

        for (int i : nums) {
            if (i < pivot) {
                less.add(i);
            } else if (i == pivot) {
                equal.add(i);
            } else {
                great.add(i);
            }
        }

        int j = 0;
        for (int i : less) {
            nums[j++] = i;
        }
        for (int i : equal) {
            nums[j++] = i;
        }
        for (int i : great) {
            nums[j++] = i;
        }

        return nums;
    }
}
