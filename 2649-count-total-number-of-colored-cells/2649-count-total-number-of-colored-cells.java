class Solution {
    public long coloredCells(int n) {
        long N = (long) n;
        return (N * N) + (N - 1) * (N - 1);
    }
}
