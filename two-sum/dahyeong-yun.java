/**
 * [문제 분석 및 풀이]
 * 1. 시간 복잡도
 * - nums.length가 최대 10^4 (1만) 이므로 O(N^2)도 아슬아슬 통과할 수 있음. 이중 루프를 의도해서 문제를 내는 경우는 희박하므로 O(N log N) 이하로 풀어보자.
 * 2. 고려 사항
 * - 배열의 인덱스를 정확히 리턴해야 하기 때문에 정렬할 수 없음.
 * - 자료형 제약 : 배열 원소의 각 값은 int 범위 내임. 
 * 3. 풀이 아이디어 : Hash
 * - 필요한 수를 value로, 그 수의 인덱스를 value 로 갖는 key-value 쌍이 있다고 하자.
 * - 두 수 x, y의 합이 target이라면 수식으로는 x + y = target 이다. 이 때 루프를 돌면서 nums[i]가 x에 대입된다면 y = target - nums[i]가 된다.
 * - key-value 쌍에서 y 값이 존재하는 지를 찾으면 된다.
 * - 자바의 HashMap은 O(1)에 값을 찾을 수 있으므로 시간 복잡도는 O(1), 공간 복잡도는 최악의 경우에 O(N)이 된다.
 */
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        int len = nums.length;
        for(int i=0; i < len; i++) {
            int y = target - nums[i];
            if(map.get(y) != null) {
                return new int[]{i, map.get(y)};
            }
            map.put(nums[i], i);
        }
        // java 문법 상 return 이 필요.
        return new int[]{};
    }
}
