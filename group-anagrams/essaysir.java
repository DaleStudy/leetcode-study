class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // 아나그램을 그룹별로 만들어라
        // 아나그램 -> 각 string 을 배치해서 만들 수 있는 가 ?
        // 각 알파벳이 몇개가 있는 가 ?
        List<List<String>> answer = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();

        for ( int i = 0;  i < strs.length; i ++) {
            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);

            String s = new String(chars);
            map.computeIfAbsent(s, k -> new ArrayList<>()).add(strs[i]);
        }

        for (List<String> group : map.values()) {
            answer.add(group);
        }

        return answer;
    }
}
