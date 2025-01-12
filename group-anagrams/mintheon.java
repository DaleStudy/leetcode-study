import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
  /**
   시간복잡도: O(n)
   공간복잡도: O(n)
   */
  public List<List<String>> groupAnagrams(String[] strs) {
    Map<String, List<String>> anagramMap = new HashMap<>();

    for(String str : strs) {
      char[] charStr = str.toCharArray();
      Arrays.sort(charStr);
      String sortedStr = String.valueOf(charStr);

      if(!anagramMap.containsKey(sortedStr)) {
        anagramMap.put(sortedStr, new ArrayList<>());

      }

      anagramMap.get(sortedStr).add(str);
    }

    return new ArrayList<>(anagramMap.values());
  }
}
