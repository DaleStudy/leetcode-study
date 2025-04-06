import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> checkList = new HashSet<>();
        int seqCnt = 0;
        int start = Integer.MIN_VALUE;

        for(int n : nums){
            checkList.add(n);
        }

        for (int n : nums) {
            int seq = 1;
            int target = n+1;
            if(checkList.contains(n-1))continue;

            while(checkList.contains(target)){
                checkList.remove(target);
                seq++;
                target++;
            }

            if(seqCnt < seq){
                seqCnt = seq;
                start = n;
            }
        }
        return seqCnt;
    }
}

