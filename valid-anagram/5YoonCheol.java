import java.util.HashMap;

public class Solution {
    public boolean isAnagram(String s, String t) {
        //HashMap 자료구조를 통해 아나그램 여부 판별
        //s,t 문자열에서 문자인 것만 HashMap에 넣어준다.
        //이때 중복인 경우 value 값을 1씩 증가시킨다.
        //Character 타입의 개수가 맞지 않으면 false
        //두 개의 Map이 서로 동일하면 아나그램이다. -> true
        //그 외의 경우는 Character의 개수가 맞지 않기 때문에 false
        HashMap<Character, Integer> sMap = new HashMap<>();
        HashMap<Character, Integer> tMap = new HashMap<>();
        for (Character c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                sMap.put(c, sMap.getOrDefault(c, 0) + 1);
            }
        }

        for (Character c : t.toCharArray()) {
            if (Character.isLetter(c)) {
                tMap.put(c, tMap.getOrDefault(c, 0) + 1);
            }
        }

        if (sMap.size() != tMap.size()) return false;
        else if (sMap.equals(tMap)) return true;
        else return false;
    }
}
