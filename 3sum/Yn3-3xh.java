/*
[문제풀이]
- nums 배열 안의 3가지 수를 더했을 때 0이어야 한다.
- 더해진 수들의 index는 모두 달라야 한다.
- DFS (X)
    StackOverflowError
- 투 포인터 (O)
time: O(N^2), space: O(N^2)

[회고]
해설을 보고 이해는 했는데 다시 풀 수 있을까?
아직 스킬이 부족한 것 같다..

*/
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> answers = new HashSet<>();
        Arrays.sort(nums);

        for (int start = 0; start < nums.length; start++) {
            int mid = start + 1;
            int end = nums.length - 1;

            while (mid < end) {
                int sum = nums[start] + nums[mid] + nums[end];
                if (sum == 0) {
                    List<Integer> answer = List.of(nums[start], nums[mid], nums[end]);
                    answers.add(answer);
                    end--;
                } else if (sum < 0) {
                    mid++;
                } else if (sum > 0) {
                    end--;
                }
            }
        }
        return new ArrayList<>(answers);
    }
}
