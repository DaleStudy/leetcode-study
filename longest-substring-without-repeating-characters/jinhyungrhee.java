import java.util.*;
class Solution {
    public int lengthOfLongestSubstring(String s) {

        if (s.length() == 0) return 0;
        if (s.length() == 1) return 1;

        // sliding window
        HashSet<Character> table = new HashSet<>();

        int left = 0;
        int right = 1;
        int end = s.length() - 1;

        table.add(s.charAt(left));

        int maxSize = 0;
        while (right <= end) {

            if (!table.contains(s.charAt(right))) {
                table.add(s.charAt(right));
            } else {
                /** [중복된 문자면 슬라이딩 윈도우 이동]
                 1. 중복 문자를 만나면 left를 한칸씩 증가
                 2. 중복 문자가 Hash 에서 사라질 때까지 왼쪽 값 제거
                 3. 왼쪽 중복문자가 제거되었을 때 right 이동
                 */
                while(table.contains(s.charAt(right))) {
                    table.remove(s.charAt(left));
                    left++;
                }
                table.add(s.charAt(right));
            }

            int tableSize = table.size();
            if (tableSize > maxSize) maxSize = tableSize;

            right++;
        }

        return maxSize;
    }

}

