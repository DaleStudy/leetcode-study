class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // 같은 문자열 끼리 묶기
        // 그룹이 가장 적은 순으로 정렬

        Map<String, List<String>> map = new HashMap<>();

        // 각 문자열 char로 바꿔서 정렬하고 다시 문자열
        for(String str : strs) {
            char[] arr = str.toCharArray();
            Arrays.sort(arr);

            String key = new String(arr); // 정렬된 문자열 키로 하기

            map.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
        }

        return new ArrayList<>(map.values());
        // map 자료구조, 정렬까지 생각 
        // 이후 프로세스 생각 어려움
    }
}
