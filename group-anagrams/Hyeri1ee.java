import java.util.*;

class Solution {
    //static HashMap<
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map  = new HashMap<>();

        for(int w = 0 ;w < strs.length; w++){
            String word = strs[w];
            char[] arr = word.toCharArray();

            //정렬한거
            Arrays.sort(arr);
            String newWord = new String(arr);

            map.putIfAbsent(newWord, new ArrayList<>());
            map.get(newWord).add(word);

        }


        List<List<String>> list = new ArrayList<>();
        for(List<String> group : map.values()){
            list.add(group);
        }

        return list;
    }
}

