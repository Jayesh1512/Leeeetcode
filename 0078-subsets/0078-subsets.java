import java.util.ArrayList;
import java.util.List;

class Solution {
    public void generate(List<Integer> arr, int idx, List<Integer> subset, List<List<Integer>> result) {
        if (idx == arr.size()) {
            result.add(new ArrayList<>(subset));
            return;
        }
        generate(arr, idx + 1, subset, result);
        subset.add(arr.get(idx));
        generate(arr, idx + 1, subset, result);
        subset.remove(subset.size() - 1);
    }

    public List<List<Integer>> subsets(int[] arr) {
        List<Integer> inputList = new ArrayList<>();
        for (int num : arr) {
            inputList.add(num);
        }

        List<Integer> subset = new ArrayList<>();
        List<List<Integer>> result = new ArrayList<>();
        generate(inputList, 0, subset, result);
        return result;
    }
}
