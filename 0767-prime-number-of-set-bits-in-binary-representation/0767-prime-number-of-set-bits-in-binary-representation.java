class Solution {
public static int countPrimeSetBits(int left, int right) {

		int count = 0;

		for (int i = left; i <= right; i++) {

			int a = i;

			int b =  Integer.bitCount(a);

			if(isPossible(b)) {
				count++;
			}
			
		}
		return count;
	}

	public static boolean isPossible(int num) {

			if(num < 2) {
				return false;
			}
			
			for (int i = 2; i * i <= num; i++) {
				if (num % i == 0) {
					return false;
				}
			}
			return true;
		}
}