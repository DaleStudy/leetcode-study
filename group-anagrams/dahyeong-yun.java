/**
  * input str의 길이가 n이고, 각 str 문자열의 길이를 m라 할 때
  * 
  * TC : O(n * m log n)
  *   - n 번 순회할 때마다 각 단어 정렬에 m log m 만큼 소요되므로 O(n * m log m)
  * SC : O(n * m)
  *   - n * m 만큼의 char 배열 공간을 key 값 생성으로 사용
  *   - 정답 Map 에서 입력 크기 n만큼의 공간 을 사용
  *   - 따라서 (n * m) + n 즉 O(n * m) 만큼의 공간 사용
  */
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> answer = new HashMap<>();

        for(String str : strs) {
            char[] c = str.toCharArray();
            Arrays.sort(c);
            String key = String.valueOf(c);
            answer.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
        }

        return new ArrayList<>(answer.values());
    }
}
