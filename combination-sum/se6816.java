/**
    중복 조합을 통해 조건에 맞는 조합을 찾는 방식
    candidates의 길이 -> N
    시간 복잡도 : O(2^N)
    공간 복잡도 : O(N)  
 */
class Solution {
    List<List<Integer>> list;
    List<Integer> dataList;
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        list = new ArrayList<>();
        dataList = new ArrayList<>();
        execute(candidates, 0, 0, target);
        return list;
    }

    public void execute(int[] candidates, int idx, int sum, int target) {
        if(idx >= candidates.length) {
            return;
        }

        if(sum == target) {
            list.add(new ArrayList<>(dataList));
            return;
        }

        if(sum+candidates[idx] > target) {
            return;
        }

        


        dataList.add(candidates[idx]);
        execute(candidates, idx, sum + candidates[idx], target);
        dataList.remove(dataList.size()-1);
        execute(candidates, idx+1, sum, target);
    }
}
