/**
[문제풀이]
- 주어진 배열에서 연속된 수 배열의 합이 큰 수 구하기
    - (1) 현재수와 현재까지의 합 중 큰 수 구하기 : 현재 인덱스부터 시작되거나, 현재 인덱스까지 더해질 것
    - (2) 최댓값과 (1)번 수 중 큰 수 구하기
time: O(N), space: O(1)

[회고]
솔루션까지는 근접하는데, 결국 해결은 자꾸 안된다..
어떻게 접근해야 솔루션까지 도달 할 수 있을까..
 */
class Solution {
    public int maxSubArray(int[] nums) {
        int max = nums[0];
        int sum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            sum = Math.max(nums[i], sum + nums[i]);
            max = Math.max(max, sum);
        }
        return max;
    }
}

