import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// NOTE: tc -> O(n)
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        List<List<String>> result = new ArrayList<>();
        Map<String, List<String>> sMap = new HashMap<>();

        for(int i = 0; i < strs.length; i++) {
            char[] cArr = strs[i].toCharArray();
            Arrays.sort(cArr);
            String sorted = new String(cArr);

            if(sMap.containsKey(sorted)) {
                sMap.get(sorted).add(strs[i]);
            } else {
                List<String> temp = new ArrayList<>();
                temp.add(strs[i]);
                sMap.put(sorted, temp);
            }
        }

        for(List<String> arr : sMap.values()) {
            result.add(arr);
        }

        return result;
    }
}
