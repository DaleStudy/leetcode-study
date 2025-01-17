import java.util.ArrayList;
import java.util.List;

public class Codec {
  String SPLIT = ":";

  // Encodes a list of strings to a single string.
  public String encode(List<String> strs) {
    StringBuilder encoded = new StringBuilder();

    for(String str : strs) {
      encoded.append(str.length()).append(SPLIT).append(str);
    }

    return encoded.toString();
  }

  // Decodes a single string to a list of strings.
  public List<String> decode(String s) {
    List<String> decoded = new ArrayList<>();

    int pointer = 0;
    while(pointer < s.length()) {
      int index = s.indexOf(SPLIT, pointer);
      int length = Integer.parseInt(s.substring(pointer, index));

      String str = s.substring(index + 1, index + 1 + length);
      decoded.add(str);

      pointer = index + 1 + length;
    }

    return decoded;
  }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));
