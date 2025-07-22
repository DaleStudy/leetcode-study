import java.util.HashSet;
import java.util.Iterator;

public class Geegong {

    public int longestConsecutive(int[] nums) {

        HashSet<Integer> setOfNums = new HashSet<>();
        int start = 0;
        int end = 0;

        // initialize
        for (int num : nums) {
            setOfNums.add(num);
            start = Math.min(start, num);
            end = Math.max(end, num);
        }

        Integer longest = 0;
        Integer current = 0;
        while (start <= end) {

            iterate(setOfNums, start, current);
            longest = Math.max(longest, current);
        }
    }

    public Integer iterate(HashSet<Integer> hashSet, Integer start, Integer currentLength) {

        if (hashSet.contains(start)) {
            currentLength++;
            iterate(hashSet, start+1, currentLength);

        } else {
            // currentLength 를 리턴해야 하나..
            return start;
        }

    }

}

