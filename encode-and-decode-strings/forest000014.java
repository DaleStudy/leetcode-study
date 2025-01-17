/*
Time Complexity: O(n)
Space Complexity: O(1)

non-ASCII 유니코드 문자를 사용함

To-Do : escaping 방법 학습하기
*/
public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < strs.size(); i++) {
            if (i > 0) {
                sb.append('\u2764');
            }
            sb.append(strs.get(i));
        }

        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        return new ArrayList<>(Arrays.asList(s.split("\u2764")));
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));
