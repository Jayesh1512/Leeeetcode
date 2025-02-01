import java.util.*;

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        generate(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private void generate(int[] nums, int idx, List<Integer> subset, List<List<Integer>> result) {
        if (idx == nums.length) {
            result.add(new ArrayList<>(subset));
            return;
        }
        subset.add(nums[idx]);
        generate(nums, idx + 1, subset, result);
        subset.remove(subset.size() - 1);  
        while (idx + 1 < nums.length && nums[idx] == nums[idx + 1]) {
            idx++;
        }
        generate(nums, idx + 1, subset, result);
    }
}
