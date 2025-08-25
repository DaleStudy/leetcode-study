class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> answer = new ArrayList<>();
        // <정렬한 문자, 원본 문자 리스트>
        HashMap<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            char[] arr = str.toCharArray();
            Arrays.sort(arr);
            String strKey = String.valueOf(arr);
            
            if (!map.containsKey(strKey)) {
                ArrayList<String> list = new ArrayList<>();
                list.add(str);
                map.put(strKey, list);
            } else {
                map.get(strKey).add(str);
            }
        }
        answer.addAll(map.values());
        return answer;
    }
}
