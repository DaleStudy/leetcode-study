import java.util.*;
/* 시간 복잡도: O(N), nums.length를 n이라고 할 때, 시간 복잡도는 O(N)
 * HashSet
 * - contains: O(1)
 * - add: O(1)
 * 
 * 공간 복잡도: O(N), Set에 최대 n개의 요소를 저장할 수 있음
 */ 
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (set.contains(num)) return true;
            set.add(num);
        }
        return false;
    }
}