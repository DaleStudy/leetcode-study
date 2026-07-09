import java.util.*;

// 시간복잡도 : O(n), 공간복잡도 : O(n)

class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length()!=t.length()){
            return false;
        }

        Map<Character,Integer> characterMap = new HashMap<>();

        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            characterMap.put(c,characterMap.getOrDefault(c,0)+1);
        }

        for(int i=0;i<t.length();i++){
            char c = t.charAt(i);

            if(!characterMap.containsKey(c)){
                return false;
            }

            characterMap.put(c, characterMap.get(c) - 1);
            if(characterMap.get(c)<0){
                return false;
            }
        }
        return true;
    }
}
