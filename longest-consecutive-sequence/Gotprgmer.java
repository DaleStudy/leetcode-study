import java.util.*;
class SolutionGotprgmer {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int num:nums){
            set.add(num);
        }
        System.out.println(set);
        int answer = 0;
        for(int num:nums){
            //왼쪽으로 확장
            int left = 0;
            while(set.contains(num-(left+1))){
                left += 1;
            }

            //오른쪽으로 확장
            int right = 0;
            while(set.contains(num+right+1)){
                right += 1;
            }
            System.out.println(String.valueOf(left)+" " + String.valueOf(right));
            answer = Math.max(answer,left+right+1);
        }

        return answer;

    }
}
