/**
 * Runtime: 6ms
 * Time Complexity: O(n x k log k)
 * - n: 문자열 개수
 * - k: 문자열 최대 길이
 * - k log k: 각 문자열을 정렬하는 시간
 *
 * Memory: 49.30MB
 * Space Complexity: O(n x k)
 * - 최대 n개의 키-값
 *
 * Approach: 정렬된 문자열을 키로 사용해서 같은 애나그램끼리 그룹화
 */
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramMap = new HashMap<>();

        for (String str: strs) {
            char[] chs = str.toCharArray();
            Arrays.sort(chs);
            String key = new String(chs);

            anagramMap.computeIfAbsent(key, k -> new ArrayList<>())
                    .add(str);
        }

        return new ArrayList<>(anagramMap.values());
    }
}
