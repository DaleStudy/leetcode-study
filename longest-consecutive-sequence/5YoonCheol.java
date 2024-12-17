import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) return 0;

        //모든 요소 HashSet 삽입
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        int longest = 0;

        // 시작지점 체크
        for (int num : nums) {
            //배열 요소보다 1 작은 수 가 없는 경우 새로운 시작 지점이 됨
            if (!set.contains(num - 1)) {
                int start = num;
                int currentLength = 1;

                // 1씩 증가시키면서 연속된 수의 개수 탐색
                while (set.contains(start + 1)) {
                    start++;
                    currentLength++;
                }
                // 기존 longest와 현재 연속된 수를 비교
                longest = Math.max(longest, currentLength);
            }
        }

        return longest;
    }
}
