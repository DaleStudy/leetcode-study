class Solution {
    //left,right

    //right를 left에서부터 이동하면서 max (대체해야되는 alphabet 수) 갱신
    //(right - left+ 1)  - 다수등장alphabet 개수 = 대체해야되는 alphabet 수
    //대체해야되는 수 <= k 인 경우 완료
    //"" > k 인 경우 left++
    
    //빈도수 저장용
    int[] alpha = new int[26];
    int answer =0 ;

    public int characterReplacement(String s, int k) {
        
        //인덱스 정의 (초기값)
        int left= 0;
        int right= 0;



        while(right < s.length()){
            //현재 갱신된 right까지 빈도수 저장
            //System.out.println("[right] : " + right);
            //System.out.println("[left] : " + left);

            alpha[s.charAt(right) - 'A']++;

            int max = mostSeenFrequency(left, right, alpha); 

            

                while ((right-left + 1) - max > k) {
                    alpha[s.charAt(left) - 'A']--;
                    left++;
                    max = mostSeenFrequency(left, right, alpha);
                }

                if (answer < right-left + 1){
                    answer=right-left+1;
                }
                right++;

                //System.out.println("[answer] : " + answer);
               
            
        }//end of while

        return answer;

    }

    private static int mostSeenFrequency(int left, int right, int[] alpha){
        int max =0;
        for(int i=0;i<26;i++){
            if (max < alpha[i]) max=alpha[i];
        }
        return max;
    }
}


