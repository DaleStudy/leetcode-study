/**
 * [문제 분석 및 풀이]
 * 1. 시간 복잡도
 * - nums.length가 최대 10^5 (10만) 이므로 O(N log N) 이하로 풀어야 함.
 * 2. 고려 사항
 * - O(N)에 풀어야 함. 그럼 정렬을 할 수가 없음.
 * - 증복값이 존재할 수 있음
 * 3. 풀이 아이디어 : 
 * - (힌트 참조 : 이중 루프라고 하더라도 꼭 O(N^2)이 아닐 수도 있음. 연속된 숫자의 처음인 경우만 다음 숫자를 센다고 치면 숫자 당 총 2번만 방문하게 되므로 최대 2N번 반복하게 됨. 그러므로 시간 복잡도 기준 O(N)이 됨)
 */
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;

        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        int max = 0;
        
        // 💡 nums 대신 중복이 제거된 set을 순회합니다!
        for (int num : set) {
            // 시작점인지 확인
            if (!set.contains(num - 1)) {
                int count = 1;
                int cursor = num;
                
                while (set.contains(cursor + 1)) {
                    cursor++;
                    count++;
                }
                max = Math.max(max, count); 
            }
        }
        return max;
    }
}
