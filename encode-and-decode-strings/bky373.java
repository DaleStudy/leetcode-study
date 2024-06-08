/**
 * time: O(N)
 * space: O(N)
 */
public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String str : strs) {
            sb.append(str.length())
              .append(':')
              .append(str);
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> decoded = new ArrayList<>();
        int i = 0;
        while (i < s.length()) {
            int searchIndex = s.indexOf(':', i);
            int chunkSize = Integer.parseInt(s.substring(i, searchIndex));
            i = searchIndex + chunkSize + 1;
            decoded.add(s.substring(searchIndex + 1, i));
        }
        return decoded;
    }
}
