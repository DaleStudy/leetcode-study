/*
1. 문제 이해
(){}[] 문자가 들어올때 순서대로 들어오는가 ?
여기서 순서란 ([)] 와 같이 섞여 있는게 아니라 ([{}])와 같이 가운데를 기준으로 들어온것이 맞는지를 말하는 것

2. 알고리즘
스택을 사용한다
이유는 이 문제를 해결할때 마지막 입력과 다음 것을 비교해야하는데
가장 마지막에 입력된 것과 들어올 것을 서로 비교하기 가장 적합한 자료구조이기 때문이다.

3. 예외
1개만 요소가 존재한다면 ?

4. 구현

각 요소에 대해 hash map 을 생성한다
스택을 두고 첫번째 값을 넣는다
그 다음부터는 순차적으로 비교하며 동일할 경우 다음 값과 마지막에 있던 값을 제거한다.


*/
import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> parens = new HashMap<>();
        parens.put('(', ')');
        parens.put('{', '}');
        parens.put('[', ']');
        Stack<Character> stack = new Stack<>();

        for (int i=0; i<s.length(); i++) {
            char cur = s.charAt(i);
            
            if (parens.containsKey(cur)) {
                stack.push(cur);
            } else {
                if (stack.isEmpty() || cur != parens.get(stack.pop())) {
                    return false;
                }
            }
        }

        if (s.length() == 1 || !stack.isEmpty()) {
            return false;
        }

        return true;
    }
}

