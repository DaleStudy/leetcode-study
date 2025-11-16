class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // 전체 시간 복잡도: O(N2), 공간 복잡도: O(N)
        // 정렬: 시간 복잡도: O(N log N)
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        // x 하나 잡아놓고, 투포인터 사용해서 y + z 가 -x 보다 크면 z 를 - 1, 적으면 y 를 + 1, y와 z가 만나면 break, y + z 가 -x 와 같으면 정답
        // 0 보다 큰 케이스는 돌 필요가 없음
        for (int i = 0; i < nums.length && nums[i] <= 0; ++i) {
            // 시간 복잡도: O(N)
            if (i == 0 || nums[i - 1] != nums[i]) {
                findThreeSum(nums, i, result);
            }
        }
        return result;
    }

    void findThreeSum(int[] nums, int i, List<List<Integer>> result) {
        // 시간 복잡도: O(N), 공간 복잡도: O(3N) = O(N)
        int left = i + 1, right = nums.length - 1;
        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];
            if (sum < 0) {
                ++left;
            } else if (sum > 0) {
                --right;
            } else {
                // 정답 케이스 찾아서 결과에 넣기
                result.add(Arrays.asList(nums[i], nums[left++], nums[right--]));
                while (left < right && nums[left] == nums[left - 1]) ++left; // 숫자 중복인 케이스 넘어가기
            }
        }
    }
}