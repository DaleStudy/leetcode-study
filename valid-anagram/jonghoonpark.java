/*
 * https://leetcode.com/problems/valid-anagram/
 * time complexity : O(nlogn)
 * space complexity : O(n)
 * https://jonghoonpark.com/2024/04/24/leetcode-242
 */


/*
import java.util.Arrays;

void main() {
    Solution solution = new Solution();
    System.out.println(solution.isAnagram("anagram", "nagaram")); // true
    System.out.println(solution.isAnagram("rat", "car")); // false
}

class Solution {
    public boolean isAnagram(String s, String t) {
        char[] temp1 = s.toCharArray();
        char[] temp2 = t.toCharArray();
        Arrays.sort(temp1);
        Arrays.sort(temp2);
        return Arrays.equals(temp1, temp2);
    }
}
*/