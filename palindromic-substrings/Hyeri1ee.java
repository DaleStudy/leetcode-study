class Solution {
    //길이 1~s.length()까지 palindrome 함수 시도
    int cnt=0; //


    public int countSubstrings(String s) {

        for(int len=1; len <= s.length();len++){//1~3
            for(int idx =0; idx <= s.length()-len ; idx++){
                //idx인덱스부터 len길이만큼의 문자열이 palindrome인지 판별
                boolean result =  isPalindrome(s, idx, idx+len-1); //start: 시작 인덱스 , end: 끝 인덱스

                if (result){
                    cnt++;
                }
            }
        }

        return cnt;

    }

    private static boolean isPalindrome(String w, int start, int end){
            if (start == end) return true;
            //start!= end
            int s = start;
            int e = end;
            while(s<= e){
                if(e < start && s > end) return true;


                //서로 값이 다른 경우
                if (w.charAt(s) != w.charAt(e)){
                    return false;
                }

                //서로 값이 같은 경우 continue;
                s++;
                e--;
            }


            return true;
    }
        
   
}


