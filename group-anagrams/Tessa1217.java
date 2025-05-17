/**
 * 문자열 배열 strs가 주어질 때 애너그램인 문자들끼리 묶어서 반환하세요.
 */
class Solution {
    // 시간복잡도: O(n * L log L)
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramMap = new HashMap<>();
        for (String str : strs) {
            char[] word = str.toCharArray();
            Arrays.sort(word);
            String sortedCharacter = String.valueOf(word);
            if (!anagramMap.containsKey(sortedCharacter)) {
                anagramMap.put(sortedCharacter, new ArrayList<>());
            }
            anagramMap.get(sortedCharacter).add(str);
        }
        return new ArrayList(anagramMap.values());
    }

}

