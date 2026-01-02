/**
 * Runtime: 26ms
 * Time Complexity: O(n)
 * - HashSet 구성: O(n)
 * - 모든 원소 순회: 최악 O(n), 평균적으로 더 빠름 (조기 종료)
 * - 연속 수열 탐색: O(n)
 *
 * Memory: 95.11MB
 * Space Complexity: O(n)
 *
 * Approach: HashSet을 이용하여 중복 제거 후 연속 수열 길이 탐색
 * - 연속 수열의 시작점만 탐색하여 중복 작업 방지 (num-1이 없는 경우)
 * - 각 시작점에서 연속된 다음 숫자들을 순차적으로 탐색
 * - nums 사이즈에 도달 시 조기 종료하여 불필요한 탐색 방지
 */
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;

        Set<Integer> set = new HashSet<>();
        for (int num: nums) {
            set.add(num);
        }

        int longestLength = 0;
        for (int num: set) {
            if (!set.contains(num-1)) {
                int currentNum = num;
                int currentLength = 1;

                while (set.contains(currentNum+1)) {
                    currentNum++;
                    currentLength++;
                }

                longestLength = longestLength < currentLength ? currentLength : longestLength;
                if (longestLength == set.size()) {
                    return longestLength;
                }
            }
        }

        return longestLength;
    }
}
