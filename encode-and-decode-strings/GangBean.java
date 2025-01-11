import java.util.*;

public class Codec {
    /**
    1. complexity:
    - time: O(N * L), where N is the length of strs, L is maximum length of each word in strs
    - space: O(N * L)
    */

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        // 필요한 정보: 전체 원본 문자열, 각 단어의 위치와 길이
        StringBuilder origin = new StringBuilder();
        StringJoiner meta = new StringJoiner("/");
        StringJoiner encoded = new StringJoiner(";");
        int startIdx = 0;
        for (String word: strs) { // O(N)
            origin.append(word);
            meta.add(String.format("(%d,%d)", startIdx, word.length()));
            startIdx += word.length();
        }

        encoded.add(origin.toString()).add(meta.toString());
        return encoded.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> ret = new ArrayList<>();
        int delimeterIdx = s.lastIndexOf(";"); // O(N * L)
        String origin = s.substring(0, delimeterIdx); // O(N * L)
        String meta = s.substring(delimeterIdx+1); // O(N * L)
        String[] wordInfos = meta.split("/");
        for (String wordInfo: wordInfos) { // O(N)
            delimeterIdx = wordInfo.indexOf(","); // O(1)
            int length = Integer.parseInt(wordInfo.substring(delimeterIdx+1, wordInfo.length() - 1)); // O(1)
            String word = "";
            if (length > 0) {
                int startIdx = Integer.parseInt(wordInfo.substring(1, delimeterIdx));
                word = origin.substring(startIdx, startIdx + length);
            }
            ret.add(word);
        }
        return ret;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));


