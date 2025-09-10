class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        rec(candidates.length - 1, target, new ArrayList<>(), ans, candidates);
        return ans;
    }

    public void rec(int i, int t, List<Integer> c, List<List<Integer>> ans, int[] candidates) {
        if (t == 0) {
            ans.add(new ArrayList<>(c)); 
            return;
        }

        if (t < 0 || i < 0) {
            return;
        }

        rec(i - 1, t, c, ans, candidates);
        c.add(candidates[i]);
        rec(i, t - candidates[i], c, ans, candidates);
        c.remove(c.size() - 1); 
}
}