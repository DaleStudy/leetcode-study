/**
 * two sum이랑 비슷한 문제
 * arraylist 사용시 timeout
 * 해시맵? 사용해보자
 */
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet set = new HashSet<>();
        for (int num : nums) {
            if(set.contains(num)) {
                return true;
            }
            set.add(num);
        }
        return false;
    }
}

