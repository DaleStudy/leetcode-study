import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

/**
 * time complexity : O(n)
 */
public class Geegong {

    public int longestConsecutive(int[] nums) {
        HashSet<Integer> setOfNums = new HashSet<>();
        // key : startIndex , value : length
        Map<Integer, Integer> lengthMap = new HashMap<>();

        // sort..? 를 해야될까 싶음..

        // initialize
        for (int num : nums) {
            setOfNums.add(num);
        }

        Integer longest = 0;

        for (Integer num : setOfNums) {
            int length = iterate(setOfNums, num, 0, lengthMap);
            longest = Math.max(longest, length);
        }

        return longest;
    }

    public Integer iterate(HashSet<Integer> hashSet, int currIndex, int currLength, Map<Integer, Integer> lengthMap) {
        if (lengthMap.containsKey(currIndex)) {
            return lengthMap.get(currIndex);
        }

        if (hashSet.contains(currIndex)) {
            currLength++;
            return iterate(hashSet, currIndex+1, currLength, lengthMap);

        } else {
            lengthMap.put(currIndex, currLength);
            return currLength;
        }

    }

}

