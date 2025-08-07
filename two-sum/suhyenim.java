/* [5th/week01] 1. Two Sum

1. 문제 요약
링크: https://leetcode.com/problems/two-sum/description/
배열 내 두 숫자의 합이 target이 되는 key들을 배열로 반환
(특이점: 답은 반드시 하나만 존재)

2. 풀이 로직
제출1: 반복문을 중첩으로 돌리면서, 두 숫자의 합이 target일 때의 두 인덱스를 배열로 반환
성공: Time: 45 ms (30.61%), Space: 44.9 MB (63.79%)
=> 시간 복잡도: O(n^2), 공간 복잡도: O(1)
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target)
                    return new int[]{i, j};
            }
        }
    return null;
    }
}

풀이2: target과의 차가 HashMap의 key들 중에 존재하면 두 인덱스를 배열로 반환, 아니라면 HashMap에 value-key쌍으로 추가
성공: 2 ms (98.95%), Space: 45.1 MB (30.45%)
=> 시간 복잡도: O(n), 공간 복잡도: O(n)
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> indices = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (indices.containsKey(complement)) {
                int j = indices.get(complement);
                return new int[]{j, i};
            }
            indices.put(nums[i], i);
        }
        return null;
    }
}

3. TIL
HashTable을 활용해서 key-value 자료구조를 구현할 수 있다.

*/

class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target)
                    return new int[]{i, j};
            }
        }
    return null;
    }
}
