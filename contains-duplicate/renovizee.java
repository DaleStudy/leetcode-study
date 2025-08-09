import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

// tag renovizee 1week
// https://github.com/DaleStudy/leetcode-study/issues/217
// https://leetcode.com/problems/contains-duplicate/
class Solution {

    //    Solv2: hash set (feedback)
    public boolean containsDuplicate(int[] nums) {
        // 시간복잡도 : O(n)
        // 공간복잡도 : O(n)
        Set<Integer> numsSet = new HashSet<>();
        for (int num : nums) {
            if (numsSet.contains(num)) {
                return true;
            }
            numsSet.add(num);
        }
        return false;
    }

//    Solv1: hash map
//    public boolean containsDuplicate(int[] nums) {
//        // 시간복잡도 : O(n)
//        // 공간복잡도 : O(n)
//        Map<Integer,Integer> countMap = new HashMap<>();
//        for (int num : nums) {
//            int count = countMap.getOrDefault(num, 0);
//            int addCount = count + 1;
//            countMap.put(num, addCount);
//            if (addCount == 2) {
//                return true;
//            }
//        }
//        return false;
//    }
}

//-------------------------------------------------------------------------------------------------------------
// 기본 문법 피드백
// 1) Map 기본 문법, ~.getOrDefault()
//-------------------------------------------------------------------------------------------------------------
