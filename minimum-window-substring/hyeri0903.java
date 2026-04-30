class Solution {
    public String minWindow(String s, String t) {
        /**
        1.prob: t문자를 포함하는 최소 길이의 substring return.
        2.constraints
        - 정답은 단 1개
        - t의 모든 문자를 포함
        - m,n length min = 1, max = 100000
        - s,t 는 uppercase or lowercase
        - 정답 없으면 emptystring "" return
        3.solution
        - brutforce, 모든 substring 구해서 t문자 포함 여부 체크, time complexity: O(n^2)
        - two pointer: right pointer 움직이다가 t문자 모두 포함하면 left pointer 옮기면서 가장 작은 사이즈의 substring 구하기, time compliexty: O(n)
        힌트 봐도 모르겠어서 풀이보고 풀었습니다 ㅜㅜ
         */

         int m = s.length();
         int n = t.length();
         String answer = "";

         if(m < n) return "";

         int left = 0, right = 0;
         int count = n; //필요한 문자 수 = t.length()
         int minLen = Integer.MAX_VALUE;
         int start = 0; //조건 만족하는 left pointer 시작 포인트

         int[] freq = new int[128];
         for(char c : t.toCharArray()) {
            freq[c]++;
         }

         while(right < m) {
          char r = s.charAt(right);
          //t 문자면 count--
          if(freq[r] > 0) {
            count --;
          }
          freq[r]--;
          right++;

            //조건 만족하면 left pointer 이동하며 minimum length 찾음
            while(count == 0) {
                //minLen update
                if(right - left < minLen) {
                    minLen = right - left;
                    start = left; //minLen 업데이트 시 Left pointer index 저장
                }
                char l = s.charAt(left);
                freq[l]++;

                //t문자(필요한 문자)이면 count 증가 (원래 값으로 복구)
                if(freq[l] > 0) count++;
                left++;
            }

         }

         if(minLen == Integer.MAX_VALUE) {
            answer = "";
         } else {
            answer = s.substring(start, start + minLen);
         }
        return answer;
    }
}
