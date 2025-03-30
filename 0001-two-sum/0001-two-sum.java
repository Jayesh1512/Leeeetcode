class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, ArrayList<Integer>> hm = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (hm.containsKey(nums[i])) {
                ArrayList<Integer> ar = hm.get(nums[i]);
                ar.add(i);
                hm.put(nums[i], ar);
            } else {
                ArrayList<Integer> ar = new ArrayList<>();
                ar.add(i);
                hm.put(nums[i], ar);
            }
        }

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (hm.containsKey(complement)) {
                ArrayList<Integer> complementIndices = hm.get(complement);
                for (int index : complementIndices) {
                    if (index != i) {
                        return new int[]{i, index};
                    }
                }
            }
        }
        return new int[0];
    }
    }