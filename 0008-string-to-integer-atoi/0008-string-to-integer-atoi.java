class Solution {
    public int myAtoi(String s) {
        s = s.trim();
        if (s.isEmpty()) return 0;  // Edge case: empty string
        
        char[] arr = s.toCharArray();
        boolean neg = false;
        int ans = 0;
        int idx = 0;

        if (arr[idx] == '-') {
            neg = true;
            idx++;
        } else if (arr[idx] == '+') {
            idx++;
        }

        ans = jesus(arr, idx, 0, neg);
        return neg ? -ans : ans;
    }

    public int jesus(char[] a, int idx, int prev, boolean neg) {
        if (idx >= a.length || a[idx] < '0' || a[idx] > '9') {
            return prev;
        }

        int digit = a[idx] - '0';
        if (prev > (Integer.MAX_VALUE - digit) / 10) {
            return neg ? Integer.MIN_VALUE : Integer.MAX_VALUE;
        }

        prev = prev * 10 + digit;
        return jesus(a, idx + 1, prev, neg);
    }
}
