/**
 * time: O(n)
 * space: O(n)
 */

import java.util.*;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> hash = new HashSet<>();

        for (int num: nums){
            if (hash.contains(num)) return true;
            hash.add(num);
        }

        return false;
    }
}

