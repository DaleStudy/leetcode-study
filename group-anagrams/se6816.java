/**
	Map을 통해 사전순으로 정렬된 문자열의 집합을 구한 뒤 그 집합들을 리턴하는 방식
	strs의 길이 -> N
	시간 복잡도 : O(N)
	공간 복잡도 : O(N)
*/
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
         Map<String, List<String>> hashMap = new HashMap<>();
         for(int i=0; i<strs.length;i++){
            char[] charArray = strs[i].toCharArray();
            Arrays.sort(charArray);
            String word = new String(charArray);
            List<String> list = hashMap.getOrDefault(word, new ArrayList<>());
            list.add(strs[i]);
            hashMap.put(word,list);
         }
         for(Map.Entry<String, List<String>> entry : hashMap.entrySet()){
            List<String> list = entry.getValue();
            result.add(list);
         }
         return result; 
    }
}



