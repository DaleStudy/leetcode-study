import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        //int[] 를 정렬
        Arrays.sort(nums);
        //maxlength를 갱신하는 식으로 
        int maxLength = 0;
        int curLength = 0 ;
        long prev = Long.MIN_VALUE;
        long cur = Long.MIN_VALUE;


        for(int i =0 ; i < nums.length; i++){

            //공통
            prev = cur;
            cur = nums[i];
            System.out.println("i: "+ i);

            //System.out.println("cur: "+ cur);
            //System.out.println("prev: "+ prev);
            if (curLength == 0) curLength++;

            if (cur == prev + 1){
                    curLength++;
                    maxLength = Math.max(maxLength, curLength);
                    //System.out.println("curLength : " + curLength);
                    //System.out.println("maxLength : " + maxLength);
            }else{//다르면 
                    System.out.println("여기");
                    

                    if (cur == prev){
                        maxLength = Math.max(maxLength, curLength);
                    }else{
                        maxLength = Math.max(maxLength, curLength);
                        curLength = 0;
                    }

                    //System.out.println("curLength : " + curLength);
                    //System.out.println("maxLength : " + maxLength);
            }


        


            
        }

        return maxLength;
        
    }
}