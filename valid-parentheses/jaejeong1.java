import java.util.HashMap;
import java.util.Stack;
import java.util.Map;

class SolutionValidParentheses {

  public boolean isValid(String s) {
    // last in first out 방식으로 처리해야하므로 스택 사용
    // 여는 문자면 put
    // 닫는 문자면 pop
    // 이 때 pop 대상이 올바른 짝인지 확인한다. 아니면 false 반환
    // 짝 확인 시 O(1)로 처리하기 위해 Map을 사용, 여는 문자와 닫는 문자를 key:value로 매핑
    // 끝까지 돌았고, 스택이 비어있으면 return true, 아니면 false 반환
    // 시간복잡도: O(N), 공간복잡도: O(N)

    Stack<Character> stack = new Stack<>();

    Map<Character, Character> matchedMap = new HashMap<>();
    matchedMap.put('(', ')');
    matchedMap.put('{', '}');
    matchedMap.put('[', ']');

    for (int i=0; i<s.length(); i++) {
      var currentChar = s.charAt(i);

      // 여는 문자
      if (matchedMap.containsKey(currentChar)) {
        stack.push(currentChar);
      } else { // 닫는 문자
        if (stack.isEmpty()) { // 여는 문자가 없을 경우 false
          return false;
        }

        var prevChar =  stack.peek();
        if (matchedMap.get(prevChar).equals(currentChar)) {
          stack.pop();
        } else { // 닫는 문자와 여는 문자 짝이 안맞을 경우 false
          return false;
        }
      }
    }

    return stack.isEmpty(); // 스택이 비어있으면 모든 짝 매칭이 완료된 것으로 true 반환
  }
}
