class Solution {
    /**
    Approach
    1. sort s, t
    2. compare them
     */
    public boolean isAnagram(String s, String t) {
        char[] sArr = s.toCharArray();
        Arrays.sort(sArr);

        char[] tArr = t.toCharArray();
        Arrays.sort(tArr);
        return String.valueOf(sArr).equals(String.valueOf(tArr));
    }

    /**
    Complexity
    1. time: O(nlogn) // use sort
    2. space: O(n) // declare char[]
     */
}
