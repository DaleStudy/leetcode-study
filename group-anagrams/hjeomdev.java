class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // 감이 안 와서 해설참조
        // 26자리 배열을 사용해서 알파벳 카운트 -> 문자열로 만들어서 Map의 키로 사용
        Map<String, List<String>> anagrams = new HashMap<>();
        for (String str : strs) {
            int[] count = new int[26];
            for (char ch : str.toCharArray()) {
                int idx = ch - 'a';
                count[idx] = count[idx] + 1;
            }
            String key = Arrays.toString(count);
            if (!anagrams.containsKey(key)) {
                anagrams.put(key, new LinkedList<>());
            }
            List<String> words = anagrams.get(key);
            words.add(str);
        }
        return new ArrayList(anagrams.values());
    }
}
