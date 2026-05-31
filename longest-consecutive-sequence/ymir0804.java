import java.util.HashSet;

class Solution  {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> numsSet = new HashSet<>();
        int maxNum = 0;
        for (int num : nums) {
            numsSet.add(num);
        }

        if (numsSet.isEmpty()) {
            return 1;
        } else if (numsSet.size() == 1) {
            return 0;
        }

        for (int num : numsSet) {
            boolean isStartPoint = !numsSet.contains(num - 1);
            if (isStartPoint) {
                int current = num;
                int length = 1;
                while (numsSet.contains(++current)) {
                    length++;
                }
                if (length > maxNum) {
                    maxNum = length;
                }
            }
        }
        return maxNum;
    }
}
