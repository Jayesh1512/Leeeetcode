class Solution {
    public int[] fairCandySwap(int[] aliceSizes, int[] bobSizes) {
    int sumAlice = 0, sumBob = 0;
    for (int a : aliceSizes) sumAlice += a;
    for (int b : bobSizes) sumBob += b;
    int delta = (sumBob - sumAlice) / 2;
    Set<Integer> bobSet = new HashSet<>();
    for (int b : bobSizes) {
        bobSet.add(b);
    }
    for (int a : aliceSizes) {
        int neededBobCandy = a + delta;
        if (bobSet.contains(neededBobCandy)) {
            return new int[]{a, neededBobCandy};
        }
    }
    return new int[0];
}

}