public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();

        for (String s : strs) {
            sb.append(s.length()).append('#').append(s);
        }

        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> res = new ArrayList<>();
        int i = 0;

        while (i < s.length()) {
            int j = i;

            // find '#'
            while (s.charAt(j) != '#') {
                j++;
            }

            int length = Integer.parseInt(s.substring(i, j));
            j++; // move past '#'

            String word = s.substring(j, j + length);
            res.add(word);

            i = j + length; // move to next encoded segment
        }

        return res;
    }
}
