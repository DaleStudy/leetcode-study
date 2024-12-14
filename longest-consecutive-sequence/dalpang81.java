//시간복잡도: O(n)
import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        int longNum = 0;

        // 각 숫자에 대해 시퀀스 시작 여부를 확인
        for (int num : numSet) {
            // num-1이 없는 경우에만 시퀀스를 시작
            if (!numSet.contains(num - 1)) {
                int currentNum = num;
                int currentLong = 1;

                // 연속된 숫자를 탐색
                while (numSet.contains(currentNum + 1)) {
                    currentNum++;
                    currentLong++;
                }

                // 가장 긴 시퀀스를 갱신
                longNum = Math.max(longNum, currentLong);
            }
        }

        return longNum;
    }
}
