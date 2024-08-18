public class Solution {
    // time complexity: O(n)
    // space complexity: O(n)
    Map<Integer, String> encode = new HashMap<>();
    /*
     * @param strs: a list of strings
     * @return: encodes a list of strings to a single string.
     */
    public String encode(List<String> strs) {
        // write your code here
        int key = 0;
        for (String str : strs) encode.put(key++, str);
        return String.valueOf(key);
    }

    /*
     * @param str: A string
     * @return: decodes a single string to a list of strings
     */
    public List<String> decode(String str) {
        // write your code here
        List<String> output = new ArrayList<>();
        int decode = 0;
        while (decode < Integer.valueOf(str)) output.add(encode.get(decode++));
        return output;
    }
}
