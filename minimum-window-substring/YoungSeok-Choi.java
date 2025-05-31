import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) {
            return "";
        }

        Map<Character, Integer> charCount = new HashMap<>();
        for (char ch : t.toCharArray()) {
            charCount.put(ch, charCount.getOrDefault(ch, 0) + 1);
        }

        int targetCharsRemaining = t.length();
        int[] minWindow = { 0, Integer.MAX_VALUE };
        int startIndex = 0;

        for (int endIndex = 0; endIndex < s.length(); endIndex++) {
            char ch = s.charAt(endIndex);
            if (charCount.containsKey(ch) && charCount.get(ch) > 0) {
                targetCharsRemaining--;
            }
            charCount.put(ch, charCount.getOrDefault(ch, 0) - 1);

            if (targetCharsRemaining == 0) {
                while (true) {
                    char charAtStart = s.charAt(startIndex);
                    if (charCount.containsKey(charAtStart) && charCount.get(charAtStart) == 0) {
                        break;
                    }
                    charCount.put(charAtStart, charCount.getOrDefault(charAtStart, 0) + 1);
                    startIndex++;
                }

                if (endIndex - startIndex < minWindow[1] - minWindow[0]) {
                    minWindow[0] = startIndex;
                    minWindow[1] = endIndex;
                }

                charCount.put(s.charAt(startIndex), charCount.getOrDefault(s.charAt(startIndex), 0) + 1);
                targetCharsRemaining++;
                startIndex++;
            }
        }

        return minWindow[1] >= s.length() ? "" : s.substring(minWindow[0], minWindow[1] + 1);
    }
}

class WrongSolution { // 알고리즘은 맞지만 시간초과 발생... O(n)의 sliding window 방식으로 풀어야 했던 문제..
    public String minWindow(String s, String t) {
        Map<Character, Integer> targetMap = new HashMap<>();
        List<Integer> candidates = new ArrayList<>();
        for (char c : t.toCharArray()) {
            targetMap.put(c, targetMap.getOrDefault(c, 0) + 1);
        }

        String minStr = null;
        for (int i = 0; i < s.length(); i++) {
            if (targetMap.containsKey(s.charAt(i))) {
                candidates.add(i);
            }
        }

        int size = candidates.size();

        while (size > 0) {
            Map<Character, Integer> windowMap = new HashMap<>(targetMap);
            int targetCnt = t.length();
            int startIdx = candidates.remove(0);
            int endIdx = -999;

            for (int i = startIdx; i < s.length(); i++) {
                char at = s.charAt(i);

                if (windowMap.containsKey(at) && windowMap.get(at) > 0) {
                    windowMap.put(at, windowMap.get(at) - 1);
                    targetCnt--;
                }

                if (targetCnt == 0) {
                    endIdx = i + 1;
                    break;
                }
            }

            if (targetCnt == 0) {
                if (minStr == null) {
                    minStr = s.substring(startIdx, endIdx);
                } else {
                    int prevSize = minStr.length();
                    minStr = prevSize < Math.abs(endIdx - startIdx) ? minStr : s.substring(startIdx, endIdx);
                }
            }

            size--;
        }

        return minStr == null ? "" : minStr;
    }
}
