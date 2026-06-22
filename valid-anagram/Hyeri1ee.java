import java.util.*;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        //s를 hashmap에 저장하고, t에서 하나씩 없애기
        HashMap<Character, Integer> maps = new HashMap<>();

        for(int i =0 ; i < s.length(); i++){
            char c = s.charAt(i);

            if (maps.containsKey(c)) maps.put(c, maps.get(c)+1);
            else maps.put(c, 1);
                
        }

        for(int i = 0; i< t.length() ;i++){
            char c = t.charAt(i);
            if (maps.containsKey(c)){
                if (maps.get(c) > 1) maps.put(c, maps.get(c) - 1);
                else maps.remove(c);
            }
        }


        if (maps.size() == 0) return true;

        return false;
       

        
    }
}
