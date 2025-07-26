import java.util.*;
// 2번째 푼 코드
class Solution {
    public int longestConsecutive(int[] nums) {
       Set<Integer> set = new HashSet<>();
        for (int n : nums) {
            set.add(n);
        }

        int cntMax = 0;
        for (int n : set) {  
            if (!set.contains(n - 1)) {
                int end = n;
                while (set.contains(end + 1)) {
                    end++;
                }
                cntMax = Math.max(cntMax, end - n + 1);
            }
        }

        return cntMax;
    }
}

// 처음 풀어본 코드
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

