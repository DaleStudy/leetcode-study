class Solution {
    /**
     * 각 문자열의 알파벳 등장 횟수를 키로 사용해
     * 같은 애너그램끼리 그룹화한다.
     *
     * 시간 복잡도: O(S)
     * 공간 복잡도: O(n)
     *
     * S: 모든 문자열 길이의 합
     * n: 문자열의 개수
     */
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();

        for (String word : strs) {
            int[] frequency = new int[26];

            // 알파벳별 등장 횟수를 계산한다.
            for (int i = 0; i < word.length(); i++) {
                frequency[word.charAt(i) - 'a']++;
            }

            // 빈도 배열을 같은 내용끼리 비교할 수 있는 키로 변환한다.
            String key = Arrays.toString(frequency);

            // 같은 키를 가진 문자열을 동일한 그룹에 추가한다.
            groups.computeIfAbsent(key, ignored -> new ArrayList<>())
                  .add(word);
        }

        return new ArrayList<>(groups.values());
    }
}
