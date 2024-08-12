// time : O(n)
// space : O(n)

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for(int i : nums) {
            if(set.contains(i)) {
                return true;
            }
            set.add(i);
        }
        return false;
    }
}

