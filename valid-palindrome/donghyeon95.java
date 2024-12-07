/* 첫 시도
	leetCode 기준 18ms
 */

class Solution {
	public boolean isPalindrome(String s) {
		// 1. remove non-alphanumeric using regex
		String alphanumeric = s.replaceAll("[^a-zA-Z0-9]", "");

		// 2. change lowerCase
		String lowerCase = alphanumeric.toLowerCase();

		// 3. compare reverse String
		return lowerCase.contentEquals(new StringBuffer(lowerCase).reverse());
	}
}