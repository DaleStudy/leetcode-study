// NOTE: 문제에서 반드시 log n 복잡도의 알고리즘을 작성하라고 했는데.. 맞았다..
// 이런걸 묻는건지... 다른 풀이 코드 보면서 복기가 필요함..
class Solution {
    public int findMin(int[] nums) {
        int min = 9876521;

        for(int i = 0; i < nums.length; i++) {
            min = Math.min(min, nums[i]);
        }

        return min;
    }
}
