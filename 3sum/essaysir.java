import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);

        Set<List<Integer>> result = new LinkedHashSet<>();

        // N C 3 조합 전부 나열
        List<List<Integer>> possible = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    possible.add(Arrays.asList(nums[i], nums[j], nums[k]));
                }
            }
        }

        // 합이 0인 것만 걸러서 Set에 넣기
        for (int i = 0; i < possible.size(); i++) {
            List<Integer> array = possible.get(i);
            int sum = 0;
            for (int cur : array) {
                sum += cur;
            }
            if (sum == 0) {
                result.add(array);   // Set이라 중복은 알아서 걸러짐
            }
        }

        // 3) 리턴할 때 List로 변환
        return new ArrayList<>(result);
    }
}
