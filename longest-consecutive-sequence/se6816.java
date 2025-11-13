/**
Problem 128 : Longest Consecutive Sequence
Summary : 
- set에 모든 숫자를 저장한다.
- 매개변수로 주어진 배열을 돌면서 해당 숫자의 이전 숫자가 set에 존재하는지 확인한다.
- 연속적인 숫자 배열의 길이를 구하고, 별도의 set에 기록한다.
- 해당 방법을 사용하면 시간복잡도가 O(N)이 된다.

*/
class Solution {
    public int longestConsecutive(int[] nums) {
        int max = 0;

        Set<Integer> set = new HashSet<>();
        for(int num : nums) {
            set.add(num);
        }
        Set<Integer> completeSet = new HashSet<>();
        for(int i = 0; i < nums.length; i++) {
            if(!set.contains(nums[i]-1) && !completeSet.contains(nums[i])){
                int sequence = getSequence(nums[i], set);
                max= Math.max(sequence, max);
                completeSet.add(nums[i]);
            }
        }

        return max;


    }

    public int getSequence(int startNum, Set<Integer> numSet) {
        int result = 1;
        while(true) {
            startNum++;
            if(!numSet.contains(startNum)) {
                break;
            }
            result++;
        }
        return result;
    }
}
