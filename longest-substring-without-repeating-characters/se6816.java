/**
    투포인터를 이용한 방식
    문자열 s의 길이 -> N
    시간 복잡도 : O(N)
    공간 복잡도 : O(N)
 */

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length()==0){
            return 0;
        }
        Set<Character> set =new HashSet<>();
        int start=0;
        int end=0;
        int maxSize=0;
        int len = s.length();
        while(start < len){
            

            for(int i=end; i < len;i++){
                char ch = s.charAt(i);
                if(set.contains(ch)){
                    end = i;
                    break;
                }
                set.add(ch);
            }

            maxSize = Math.max(maxSize, set.size());
            set.remove(s.charAt(start));
            start++;
        
        }
        return maxSize;
    }
}
