/*
[문제풀이]
time: O(N), space: O(N)
- 중복 제거
- 연속된 횟수 max 구하기
-- 연속된 숫자 그룹 중 첫번째부터 시작되도록

[회고]
연속된 숫자 그룹 중 첫번째부터 시작되도록 하는 부분에서 막혔다..
차분히 생각해보면 무리없이 풀 수 있지 않았을까..
*/
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        Set<Integer> numsSet = new HashSet<>();
        for (int num : nums) {
            numsSet.add(num);
        }

        int maxCount = 1;
        for (int num : numsSet) {
            if (!numsSet.contains(num - 1)) {
                int count = 1;
                int currentNum = num;
                while (numsSet.contains(currentNum + 1)) {
                    count++;
                    currentNum++;
                }
                maxCount = Math.max(maxCount, count);
            }
        }
        return maxCount;
    }
}
