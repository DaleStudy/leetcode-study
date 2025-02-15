class Solution {
    /**
    1. understanding
    - [a] -> [a,b] -> [a,b,c] -> [a] -> [a,b] -> [a,b,c] -> [b] -> [b]
    2. complexity
    - time: O(N)
    - space: O(N)
     */
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int right = 0;
        int len = s.length();
        HashSet charSet = new HashSet();
        int ret = (len==0)?0:1;
        while (left<len && right<len) {
            if (left == right) {
                right++;
                charSet = new HashSet();
                charSet.add(s.charAt(left));
            } else {
                if (!charSet.contains(s.charAt(right))) {
                    charSet.add(s.charAt(right));
                    int tmpLen = right - left + 1;
                    if (tmpLen > ret) {
                        ret = tmpLen;
                    }
                    right++;
                } else {
                    left++;
                    right = left;
                }
            }
        }

        return ret;
    }
}

