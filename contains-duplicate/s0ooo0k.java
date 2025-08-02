/*
 * 시간복잡도 O(n)
 * 공간복잡도 O(n)
 */
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for(int n : nums) {
            if(set.contains(n)){
                return true;
            }
            set.add(n);
        }
        return false;
    }
}


