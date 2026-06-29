/**
 * [문제 분석 및 풀이]
 * 1. 시간 복잡도
 * - nums.length가 최대 10^5 (10만) 이므로 O(N log N) 이하로 풀어야 함.
 * 2. 고려 사항
 * - 특별한 제약은 없지만, 정답이 unique 하다는 조건이 있음 -> 서로 다른 수가 동일한 갯 수만큼 있지 않다는 의미.
 * 3. 풀이 아이디어 : 
 * - 모든 수의 갯수를 세어서, 갯 수 값을 기준으로 역순으로 정렬한 다음 k개 만 출력하면 될 것 같음.
 * - (힌트 참조 : map에서 값 기준 정렬하기)
 */
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (map.get(nums[i]) != null)
                map.put(nums[i], map.get(nums[i])+1);
            else
             map.put(nums[i], 1);
        }
        return map.entrySet()
                .stream()
                .sorted(Map.Entry.<Integer, Integer>comparingByValue().reversed())
                .limit(k)
                .mapToInt(Map.Entry::getKey)
                .toArray();
    }
}
