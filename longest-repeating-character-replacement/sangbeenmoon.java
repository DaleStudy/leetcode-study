import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

class Solution {

    Map<Character, Integer> counterMap = new HashMap<>();

    public int characterReplacement(String s, int k) {
        
        int left = 0;
        int answer = 0;

        for (int right = 0; right < s.length(); right++){  
            if(counterMap.containsKey(s.charAt(right))){
           
                int cnt = counterMap.get(s.charAt(right));
                counterMap.put(s.charAt(right), cnt + 1);
            }
            else {
                counterMap.put(s.charAt(right), 1);
            }

            while (!isCounterOK(k)) {
                char l = s.charAt(left);
                int cnt = counterMap.get(l);
                if (cnt == 1) counterMap.remove(l);
                else counterMap.put(l, cnt - 1);
                left++;
            }
            answer = Math.max(answer, right - left + 1);
        }

        return answer;
    }

    public boolean isCounterOK(int k) {
        int maxCount = 0;
        int totalCount = 0;
        for (Entry<Character, Integer> entry : counterMap.entrySet()) {
            maxCount = Math.max(maxCount, entry.getValue());
            totalCount = totalCount + entry.getValue();
        }
        return totalCount - maxCount <= k;
    }
}
