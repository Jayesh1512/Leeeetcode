class Solution {
    public int[] plusOne(int[] digits) {
        int[] ans;
        // FIX 1: Check if there is any carry required in general, not just if digits[0] == 9
        boolean needsExtraDigit = true;
        for (int digit : digits) {
            if (digit != 9) {
                needsExtraDigit = false;
                break;
            }
        }

        // If all digits are 9, we need extra space
        if (needsExtraDigit) {
            ans = new int[digits.length + 1];
        } else {
            ans = new int[digits.length];
        }

        int carry = 0;
        ans[ans.length - 1] = digits[digits.length - 1] + 1;

        // FIX 2: Use >= 10 instead of > 10
        if (ans[ans.length - 1] >= 10) {
            ans[ans.length - 1] = ans[ans.length - 1] % 10;
            carry = 1;
        }

        for (int i = digits.length - 2; i >= 0; i--) {
            int ansIndex = i + (ans.length - digits.length); 
            if (digits[i] + carry >= 10) {
                ans[ansIndex] = (digits[i] + carry) % 10;
                carry = 1;
            } else {
                ans[ansIndex] = digits[i] + carry;
                carry = 0;
            }
        }
        if (carry == 1 && ans.length > digits.length) {
            ans[0] = 1;
        }
        return ans;
    }
}
