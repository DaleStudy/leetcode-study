/* [5th/week02] 242. Valid Anagram

1. 문제 요약
링크: https://leetcode.com/problems/valid-anagram/description/
문자열 t가 문자열 s의 anagram이면 true 반환

2. 문제 풀이
제출1: 길이가 다른지 우선 체크하고 -> 각 문자열을 배열로 만들어서 오름차순 정렬 후, 반복문을 돌면서 문자가 다르면 false 반환
성공: Time: 3 ms (91.78%), Space: 44.6 MB (43.28%)
=> 시간 복잡도: O(nlogn), 공간 복잡도: O(n)

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        char[] ss = s.toCharArray();
        char[] tt = t.toCharArray();
        Arrays.sort(ss);
        Arrays.sort(tt);
        for (int i = 0; i < s.length(); i++){
            if (ss[i] != tt[i]){
                return false;
            }
        }
        return true;
    }
}

풀이2: 길이가 다른지 우선 체크하고 -> s를 {문자:횟수} 구조의 HashMap으로 만든 후 -> t의 문자들과 비교해서 같으면 {키:밸류}쌍 삭제 -> 최종적으로 {키:밸류}쌍이 0개면 true 반환
성공: Time: 15 ms (25.19%), Space: 45 MB (10.95%)
=> 시간 복잡도: O(n), 공간 복잡도: O(n)

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> count = new HashMap<>();
        for (char c : s.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            if (!count.containsKey(c)) {
                return false;
            }
            count.put(c, count.get(c) - 1);
            if (count.get(c) == 0) {
                count.remove(c);
            }
        }

        return count.isEmpty();
    }
}

3. TIL
Map에는 다양한 메소드가 있다. ex) getOrDefault(), containsKey(), put(), get(), remove() 등
getOrDefault() 내부 구현에는 containsKey()가 사용된다.

*/

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        char[] ss = s.toCharArray();
        char[] tt = t.toCharArray();
        Arrays.sort(ss);
        Arrays.sort(tt);
        for (int i = 0; i < s.length(); i++){
            if (ss[i] != tt[i]){
                return false;
            }
        }
        return true;
    }
}
