public class Solution {
    /*
     * @param strs: a list of strings
     * @return: encodes a list of strings to a single string.
     */
    public String encode(List<String> strs) {
        // write your code here
        return strs.parallelStream()
                .map(s ->
                    s.chars()
                            .parallel()
                            .mapToObj(c -> new StringBuilder(String.format("%02x", c)))
                            .collect(
                                StringBuilder::new,
                                StringBuilder::append,
                                (a, b) -> a.append(b)
                            )
                ).collect(
                    StringBuilder::new,
                    (a, b) -> a.append(b)
                            .append(' '),
                    (a, b) -> a.append(b)
                ).toString();
    }

    /*
     * @param str: A string
     * @return: decodes a single string to a list of strings
     */
    public List<String> decode(String str) {
        // write your code here
        final List<String> ans = new ArrayList<>();
        final StringTokenizer st = new StringTokenizer(str);
        while (st.hasMoreTokens()) {
            final String s = st.nextToken();
            final StringBuilder sb = new StringBuilder();
            for (int i = 0; i < s.length(); i += 2) {
                sb.append((char) Integer.parseInt(s.substring(i, i + 2), 16));
            }
            ans.add(sb.toString());
        }
        return ans;
    }
}
