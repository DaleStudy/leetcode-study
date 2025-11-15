import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

/**
 * time complexity : O(n)
 */
public class Geegong {

    /**
     * Time complexity : O(N) + O(N long N) + O(N)
     *    - o(N) : 한번 순회해서 set
     *    - O(N log N) : sorting
     *    - O (N) : sorting된걸 한번 더 순회
     * Space complexity : O(N) -> hash set
     * @param nums
     * @return
     */
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        // hashSet
        HashSet<Integer> hashSet = new HashSet<>();
        for (int num : nums) {
            hashSet.add(num);
        }

        int[] sortedNums = hashSet.stream().mapToInt(val -> val).sorted().toArray();

        int maxLength = 1;
        int currentLength = 1;
        int prev = sortedNums[0];
        for(int index=1; index<sortedNums.length; index++) {
            int current = sortedNums[index];
            if (current == prev + 1) {
                currentLength++;

            } else {
                maxLength = Math.max(currentLength, maxLength);
                currentLength = 1;
            }

            prev = sortedNums[index];
        }



        return Math.max(currentLength, maxLength);















    }
//        HashSet<Integer> setOfNums = new HashSet<>();
//        // key : startIndex , value : length
//        Map<Integer, Integer> lengthMap = new HashMap<>();
//
//        // sort..? 를 해야될까 싶음..
//
//        // initialize
//        for (int num : nums) {
//            setOfNums.add(num);
//        }
//
//        Integer longest = 0;
//
//        for (Integer num : setOfNums) {
//            int length = iterate(setOfNums, num, 0, lengthMap);
//            longest = Math.max(longest, length);
//        }
//
//        return longest;
//    }
//
//    public Integer iterate(HashSet<Integer> hashSet, int currIndex, int currLength, Map<Integer, Integer> lengthMap) {
//        if (lengthMap.containsKey(currIndex)) {
//            return lengthMap.get(currIndex);
//        }
//
//        if (hashSet.contains(currIndex)) {
//            currLength++;
//            return iterate(hashSet, currIndex+1, currLength, lengthMap);
//
//        } else {
//            lengthMap.put(currIndex, currLength);
//            return currLength;
//        }
//
//    }

}

