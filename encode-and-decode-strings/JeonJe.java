import java.util.*;

// TC: O(n)
// SC: O(n)
class Solution {

    private static final String DELIMITER = ",";

    // ["mydata"] -> "6,mydata"
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            sb.append(s.length()).append(DELIMITER).append(s);
        }
        return sb.toString();
    }

    // "6,mydata" -> ["mydata"]
    public List<String> decode(String str) {
        List<String> answer = new ArrayList<>();

        int cursor = 0;
        while (cursor < str.length()) {
            int indexOfDelimiter = str.indexOf(DELIMITER, cursor);
            int dataStart = indexOfDelimiter + 1;
            int dataLength = Integer.parseInt(str.substring(cursor, indexOfDelimiter));

            answer.add(str.substring(dataStart, dataStart + dataLength));
            cursor = dataStart + dataLength;
        }

        return answer;
    }
}
