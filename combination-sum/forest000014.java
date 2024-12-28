/* 
time complexity: O(nlogn)
- nums 배열(=candidates) 정렬: O(nlogn)
- 재귀 호출 부분은 시간 복잡도를 계산하기가 어렵네요.. candidates 배열을 정렬해두어서, target까지 남은 차이가 현재 확인하고 있는 candidate보다 작다면 루프를 빠져나오게 해서 O(n^t)보다는 작을 텐데, 이런 경우에는 어떻게 표현해야 적절한지 잘 모르겠습니다.

space complexity: O(1) - 정답으로 사용한 이중 List는 제외

*/

class Solution {
    ArrayList<Integer> nums;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        nums = Arrays.stream(candidates)
                .boxed()
                .collect(Collectors.toCollection(ArrayList::new));

        Collections.sort(nums);

        return calc(target, 0);
    }

    private List<List<Integer>> calc(int target, int curr) {
        if (target == 0) {
            ArrayList<List<Integer>> lists = new ArrayList<>();
            lists.add(new ArrayList<>());
            return lists;
        }

        List<List<Integer>> ret = new ArrayList<>();
        boolean found = false;
        for (int i = curr; i < nums.size() && nums.get(i) <= target; i++) {
            List<List<Integer>> results = calc(target - nums.get(i), i);
            for (List<Integer> result : results) {
                result.add(nums.get(i));
                ret.add(result);
            }
        }
        return ret;
    }
}
