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
      answer.append(SEPERATOR)
          .append(str.length())
          .append(str);
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
    var i = 0;
    while (i < str.length()) {
      var seperatorIdx = str.indexOf(SEPERATOR, i) + 1;
      var size = Integer.parseInt(str.substring(seperatorIdx, seperatorIdx + 1));
      i = seperatorIdx + size + 1;
      answer.add(str.substring(seperatorIdx + 1, i));
    }

    return answer;
  }
}
