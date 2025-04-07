/*
[문제풀이]
time: O(N), space: O(N)
- nums 배열에 있는 두 수를 더한 값 = target
- 더할 때 한 번씩만 사용

[회고]
O(N^2) 보다 줄일 수 있을까?
결국 힌트3 까지 봐버렸다..

nums 배열을 돌며 target-nums[i] 값을 key로, i를 value로, HashMap에 저장하면,
배열을 돌다 해당 index의 값 nums[i]가 HashMap의 key와 일치하면,
그 key의 value인 index를 뽑으면 된다.
(Hash Table을 사용하면 키를 해싱하여 접근하기 때문에 조회가 빠르다!)

유사한 문제가 나올 때 2중 for문이 이런 접근 방식이 먼저 떠올랐으면 좋겠다.
*/

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (seen.containsKey(diff)) {
                return new int[]{seen.get(diff), i};
            }
            seen.put(nums[i], i);
        }
        return null;
    }
}
