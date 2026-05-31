class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        /**
        1.anagram 끼리 그룹화해서 return
        2.조건
        - answer in any order
        - strs 길이 최소 = 1, 최대 = 10^4
        - 원소 하나당 길이 최소 = 0, 최대 = 100
        - 모두 소문자로 구성
        3.풀이
        - 1) i번째 이후 단어를 비교해가면서 anagram check, time: O(n^2)
        - 2) HashMap: string element 를 정렬해서 key 로 사용, 중복되는 Key 있으면 anagram, time: O(n)
         */

         int n = strs.length;
         //anagram 체크할 Map
         Map<String, List<String>> map = new HashMap<>();

         for(int i = 0; i < n; i++) {
            String curStr = strs[i];
            char[] tmp = curStr.toCharArray();
            Arrays.sort(tmp);
            String key = new String(tmp);
            //  System.out.println("curStr:" + curStr + ", key: " + key);
            //Map 에 저장
            map.putIfAbsent(key, new ArrayList<>());
            map.get(key).add(curStr);
            // if(!map.containsKey(key)) {
            //     List<String> words = new ArrayList<>();
            //     words.add(curStr);
            //     map.put(key, words);
            // } else {
            //     List<String> words = map.get(key);
            //     words.add(curStr);
            //     map.put(key, words);
            // }
         }

        
         return new ArrayList<>(map.values());
    }
}
