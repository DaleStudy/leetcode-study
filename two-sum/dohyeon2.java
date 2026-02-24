import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Approach : using HashMap to get index with the element in O(n) time complexity
        // SpaceComplexity is also O(n)
        HashMap<Integer,Integer> numIndexMap = new HashMap<Integer,Integer>();

        // Make key and value HashMap
        for(int i = 0; i < nums.length; i++){
            int num = nums[i];
            numIndexMap.put(num,i);
        }

        // Search for the other operand looping nums
        for(int i = 0; i < nums.length; i++){
            int num = nums[i];
            int operand = target - num;
            Integer index = numIndexMap.get(operand);
            boolean indexExists = index != null;
            boolean indexExistsAndIndexIsNotTheNum = indexExists && i != index;
            if(indexExistsAndIndexIsNotTheNum){
                // Manual sort
                if( i < index){
                    return new int[]{ i, index };
                }else{
                    return new int[]{ index, i };
                }
            }
        }

        // If the valid answer is always exists this is not needed
        // But the compiler don't know about that
        return new int[2];
    }
}