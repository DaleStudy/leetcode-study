class Solution {

    // anagram
    // 문자열의 순서를 바꾸면 다른 단어가 되는 것
    // ex) eat, ate, tea

    /**
     * 문자열이 비어있는 경우
     * 문자열의 길이가 서로 다른 경우
     *
     * 같은 단어가 존해랄 수 있으므로 Set은 안될것 같음...
     * 두 문자열을 비교하기 위해 for loop로 순회하기에는 O(n^2) 으로 시간초과가 날것 같음...
     *
     * Map으로 key에 문자열 s에 대한 1글자당 카운트를 저장하고
     * 해당 Map을 문자열 t를 순회하면서 1글자당 카운트를 -1 하고 카운트가 0이되면 해당 key를 지운다.
     *
     * Map에 존재하지 않는 경우는 anagram이 성립할 수 없으므로 false
     *
     * Map을 이용하면 데이터를 조회 하는 경우는 O(1)이지만 결국 문자열 전체를 순회해야 하므로 O(n)
     * @param s
     * @param t
     * @return
     */
    public static boolean containsDuplicate(String s, String t) {
        if (s.length() != t.length()) return false;
        Map<Character, Integer> map = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char word = s.charAt(i);
            map.put(word, (map.getOrDefault(word, 0) + 1));
        }

        for (int i = 0; i < t.length(); i++) {
            char word = t.charAt(i);
            if (!map.containsKey(word)) {
                return false;
            }

            if (map.get(word) != 0) {
                int v = map.get(word) - 1;
                if (v == 0) {
                    map.remove(word);
                } else {
                    map.put(word, v);
                }
            }
        }

        return map.isEmpty();
    }
}
