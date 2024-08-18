import java.util.ArrayList;
import java.util.List;

class SolutionEncodeAndDecodeStrings {
  private static final char SEPERATOR = '/';
  /*
   * @param strs: a list of strings
   * @return: encodes a list of strings to a single string.
   */
  // 풀이: 문자열 길이를 구분자와 함께 encode해 decode시 문자열 길이를 참고할 수 있도록 한다
  // 시간복잡도: O(N), 공간복잡도: O(1)
  public String encode(List<String> strs) {
    // write your code here
    var answer = new StringBuilder();

    for (var str : strs) {
      answer.append(str.length())
          .append(str)
          .append(SEPERATOR);
    }

    return answer.toString();
  }

  /*
   * @param str: A string
   * @return: decodes a single string to a list of strings
   */
  // 풀이: 문자열 길이를 구분자와 함께 encode해 decode시 문자열 길이를 참고할 수 있도록 한다
  // 시간복잡도: O(N), 공간복잡도: O(N)
  public List<String> decode(String str) {
    // write your code here
    List<String> answer = new ArrayList<>();
    var charArray = str.toCharArray();
    for (int i=0; i<charArray.length; i++) {
      if (charArray[i] == SEPERATOR) {
        var size = (int) charArray[i-1];
        char[] word = new char[size];
        System.arraycopy(charArray, i + 1, word, 0, size);

        i+=size;
        answer.add(String.valueOf(word));
      }
    }

    return answer;
  }
}