/**
Problem 1 : Two Sum
Summary : 
- for문으로 순회하면서, target에서 뺀 값을 저장한다.
- 저장된 값과 일치하는 인덱스를 만나면 해당 값을 리턴한다.
- 기본 For문이 O(N^2)이라면, 해당 방법의 경우 O(N)이 가능하다. 

*/

class Solution {

    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> indexMap = new HashMap<>();
        int[] result = null;
        for(int idx=0; idx<nums.length; idx++) {
            if(indexMap.containsKey(nums[idx])) {
                result = new int[]{ indexMap.get(nums[idx]), idx };
                break;
            }
            indexMap.put(target-nums[idx], idx);
        }
        return result;
    }
}
