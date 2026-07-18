import java.util.*;

class Solution {
    public boolean isAnagram(String s, String t) {
        // 둘이 anagram 이면 인지 아닌지 확인 해라
        // 아나 그램이 다시 만들 수 있는 가 == 들어있는 알파벳의 갯수가 동일한 가
        Map<Character,Integer> prevMap = new HashMap<>();
        Map<Character,Integer> curMap = new HashMap<>();

        for ( int i = 0; i < s.length(); i++ ){
            prevMap.merge(s.charAt(i), 1, Integer::sum);
        }

        for ( int i = 0; i < t.length(); i ++){
            curMap.merge(t.charAt(i),1 ,Integer::sum);
        }

        return prevMap.equals(curMap);
    }
}
