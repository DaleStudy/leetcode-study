/**
 *  시간 복잡도: O (m * n)
 *  - m: 문자열 개수
 *  - n: 각 문자열 길이
 *  - 각 문자열에서 빈도수 계산을 위해 O(n)이 소요되는데, 이를 각 문자열마다 진행
 *
 *  공간 복잡도: O (m * n)
 *  - m: 문자열 개수
 *  - n: 각 문자열 길이
 *  - 주어진 모든 문자열이 모두 서로 anagram을 구성하지 못한 경우, 모든 문자열 수만큼 필요함
 */
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for (String str: strs) {
            int[] count = new int[26];
            for (int i = 0; i < str.length(); i++) {
                count[str.charAt(i) - 'a']++;
            }

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 26; i++) {
                sb.append("^").append(count[i]);
            }
            String candidate = sb.toString();
            if (!map.containsKey(candidate)) {
                map.put(candidate, new ArrayList<>());
            }
            map.get(candidate).add(str);
        }

        return new ArrayList<>(map.values());
    }
}
