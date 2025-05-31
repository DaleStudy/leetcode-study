
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private Map<String, Integer> memo = new HashMap<>();

    public int longestCommonSubsequence(String t1, String t2) {
        return lcs(0, 0, t1, t2);
    }

    private int lcs(int i, int j, String t1, String t2) {
        if (i == t1.length() || j == t2.length()) {
            return 0;
        }

        String key = i + "," + j;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        int res;
        if (t1.charAt(i) == t2.charAt(j)) {
            res = 1 + lcs(i + 1, j + 1, t1, t2);
        } else {
            res = Math.max(lcs(i + 1, j, t1, t2), lcs(i, j + 1, t1, t2));
        }

        memo.put(key, res);
        return res;
    }
}

class WrongSolution {
    public int longestCommonSubsequence(String t1, String t2) {
        Map<Integer, List<Integer>> sMap = new HashMap<>();
        int cnt = 0;

        // t1의 연속으로 등장하는 문자열을 하나로만 바꾸기 (e.g. abbbvvvvssssmmmddd -> abvsmd)
        StringBuilder sb = new StringBuilder();
        char start = t1.charAt(0);
        sb.append(start);
        for (int i = 1; i < t1.length(); i++) {
            if (start != t1.charAt(i)) {
                sb.append(t1.charAt(i));
                start = t1.charAt(i);
            }
        }

        t1 = sb.toString();

        for (int i = 0; i < t1.length(); i++) {
            sMap.computeIfAbsent(t1.charAt(i) - 97, k -> new ArrayList<>()).add(i);
        }

        StringBuilder filtered = new StringBuilder();
        for (int i = 0; i < t2.length(); i++) {
            int alpIdx = t2.charAt(i) - 97;
            if (sMap.containsKey(alpIdx)) {
                filtered.append(t2.charAt(i));
            }
        }
        t2 = filtered.toString();

        int prevT1Idx = -1;
        for (int i = 0; i < t2.length(); i++) {
            int alpIdx = t2.charAt(i) - 97;

            List<Integer> idxList = sMap.get(alpIdx);
            if (idxList == null)
                continue;

            for (int idx : idxList) {
                if (idx > prevT1Idx) {
                    cnt++;
                    prevT1Idx = idx;
                    break;
                }
            }
        }

        return cnt;
    }
}
