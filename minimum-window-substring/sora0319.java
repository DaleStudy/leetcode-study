public class sora0319 {
    public class Solution {
        public String minWindow(String s, String t) {
            if (s.length() < t.length()) return "";

            Map<Character, Integer> tCounts = new HashMap<>();
            Map<Character, Integer> wCounts = new HashMap<>();

            // tCounts 초기화
            for (char ch : t.toCharArray()) {
                if (tCounts.containsKey(ch)) {
                    tCounts.put(ch, tCounts.get(ch) + 1);
                } else {
                    tCounts.put(ch, 1);
                }
            }

            int minLow = 0;
            int minHigh = s.length();
            int low = 0;
            boolean found = false;

            for (int high = 0; high < s.length(); high++) {
                char ch = s.charAt(high);
                if (wCounts.containsKey(ch)) {
                    wCounts.put(ch, wCounts.get(ch) + 1);
                } else {
                    wCounts.put(ch, 1);
                }

                while (isExist(wCounts, tCounts)) {
                    if (high - low < minHigh - minLow) {
                        minLow = low;
                        minHigh = high;
                        found = true;
                    }

                    char lowChar = s.charAt(low);
                    if (tCounts.containsKey(lowChar)) {
                        int count = wCounts.get(lowChar);
                        if (count == 1) {
                            wCounts.remove(lowChar);
                        } else {
                            wCounts.put(lowChar, count - 1);
                        }
                    } else {
                        if (wCounts.containsKey(lowChar)) {
                            int count = wCounts.get(lowChar);
                            if (count == 1) {
                                wCounts.remove(lowChar);
                            } else {
                                wCounts.put(lowChar, count - 1);
                            }
                        }
                    }

                    low++;
                }
            }

            if (found) {
                return s.substring(minLow, minHigh + 1);
            } else {
                return "";
            }
        }

        private boolean isExist(Map<Character, Integer> window, Map<Character, Integer> target) {
            for (Map.Entry<Character, Integer> entry : target.entrySet()) {
                char ch = entry.getKey();
                int required = entry.getValue();

                if (!window.containsKey(ch)) {
                    return false;
                }

                int count = window.get(ch);
                if (count < required) {
                    return false;
                }
            }
            return true;
        }
    }
}


