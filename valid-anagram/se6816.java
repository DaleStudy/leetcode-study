/**
    풀이 :
        Map을 이용하여 두 문자열의 문자들의 횟수를 저장하고 비교하는 것

    복잡도 계산 :
        문자의 길이 -> N
        시간 복잡도 : O(N)
        공간 복잡도 : O(N)
*/
class Solution1 {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> targetMap = new HashMap<>();
        Map<Character, Integer> diffMap = new HashMap<>();
        calculate(s, targetMap);
        calculate(t, diffMap);
        if(isSameMap(targetMap, diffMap)) {
            return true;
        } else {
            return false;
        }
    }

    public void calculate(String s, Map<Character, Integer> map) {
        for(int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
    }

    public boolean isSameMap(Map<Character, Integer> map, Map<Character, Integer> targetMap) {
        if(map.size() != targetMap.size()) {
            return false;
        }

        for(Character key : map.keySet()) {
            if(!map.get(key).equals(targetMap.get(key))) {
                return false;
            }
        }

        return true;
    }

}
/**
    풀이 :
        알파벳 문자 횟수를 저장하는 배열을 만들고, 두 문자열의 문자르 순회하면서 합을 구함.

    복잡도 계산 :
        문자의 길이 -> N
        시간 복잡도 : O(N)
        공간 복잡도 : O(1)
*/

class Solution2 {
    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length()) {
            return false;
        }

        int[] alphbet = new int[26];

        for(int i = 0; i< s.length(); i++) {
            int idx = s.charAt(i) - 'a';
            alphbet[s.charAt(i) - 'a']++;

            int idx2 = t.charAt(i) - 'a';
            alphbet[idx2]--;
        }

        for(int i = 0; i < 26; i++) {
            if(alphbet[i] != 0) {
                return false;
            }
        }

        return true;
    }

}
