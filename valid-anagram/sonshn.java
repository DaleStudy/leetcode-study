import java.util.*;

/**
 * String to char array, sort, and compare
 * 
 * 시간 복잡도: O(nlogn)
 * 공간 복잡도: O(n)
 */
class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        Arrays.sort(sArray);
        Arrays.sort(tArray);

        return Arrays.equals(sArray, tArray);
    }
}
