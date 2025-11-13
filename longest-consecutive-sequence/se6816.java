/**
Problem 128 : Longest Consecutive Sequence
Summary : 
- for문으로 순회하면서, target에서 뺀 값을 저장한다.
- 저장된 값과 일치하는 인덱스를 만나면 해당 값을 리턴한다.
- 기본 For문이 O(N^2)이라면, 해당 방법의 경우 O(N)이 가능하다. 

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
