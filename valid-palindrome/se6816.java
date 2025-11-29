/**
      투포인터 방식을 통해 맨 앞과 맨 끝 포인터에서 맨 끝 포인터가 맨 앞 포인터를 앞지를 때까지 비교하는 방식
      문자열 s의 길이 -> N
      시간 복잡도 : O(N)
      공간 복잡도 : O(1)
 */
class Solution {
    public boolean isPalindrome(String s) {
        s=s.toUpperCase();
        int start=0;
        int end=s.length()-1;
        while(start < end){
            char ch=s.charAt(start);
            char ch2=s.charAt(end);

            // 문자 체크
            if(!((ch>=65 && ch<=90) || (ch>=48 && ch<=57))){
                start++;
                continue;
            }
            if(!((ch2>=65 && ch2<=90) || (ch2>=48 && ch2<=57))){
                end--;
                continue;
            }

            if(ch==ch2){
                start++;
                end--;
                continue;
            }

            return false;

        }
        return true;
    }
}
