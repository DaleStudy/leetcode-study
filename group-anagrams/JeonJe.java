import java.util.*;

// TC: O(n * k log k)
// SC: O(n * k)
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> answer = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            String sortedStr = String.valueOf(charArray);

            map.computeIfAbsent(sortedStr, k -> new ArrayList<>()).add(str);
        }

        for (String s : map.keySet()) {
            answer.add(map.get(s));
        }

        return answer;
    }
}
