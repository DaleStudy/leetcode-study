public class Solution {
    /*
     * @param strs: a list of strings
     * @return: encodes a list of strings to a single string.
     */
    public String encode(List<String> strs) {
        // write your code here
        StringBuilder sb = new StringBuilder();
        for (String str : strs) {
            sb.append(str.length()).append("#").append(str);
        }
        return sb.toString();
    }

    /*
     * @param str: A string
     * @return: decodes a single string to a list of strings
     */
    public List<String> decode(String str) {
        // write your code here
        List<String> output = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int idx = str.indexOf('#', i);
            int length = Integer.parseInt(str.substring(i, idx));
            String s = str.substring(idx + 1, idx + 1 + length);
            output.add(s);
            i = idx + 1 + length;
        }
        return output;
    }
}
