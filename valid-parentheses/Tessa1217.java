/**
 * 유효한 괄호: '(', ')', '{', '}', '[', ']'로 이루어진 문자열 s가 주어질 때 문자열 s가 유효한 괄호로 이루어진 문자열인지 판별하세요.
 유요한 문자열인지의 판별 방법
 1. 여는 괄호는 반드시 같은 종류의 닫는 괄호에 의해 닫혀야 한다.
 2. 여는 괄호는 반드시 정확한 순서로 닫혀야 한다.
 3. 모든 닫는 괄호는 같은 종류의 여는 괄호에 의해서 열려야 한다.
 */
class Solution {

    // 시간복잡도: O(n)
    public boolean isValid(String s) {

        Stack<Character> parentheses = new Stack<>();
        // 맵으로 조건문 간소화
        Map<Character, Character> parenthesisMap = Map.of(')', '(', '}', '{', ']', '[');

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                parentheses.push(c);
            } else if (parentheses.isEmpty() || parentheses.pop() != parenthesisMap.get(c)) { // 전체 다 돌지 않고 유효한 괄호 아니면 사전에 불린 반환
                return false;
            }
        }

        return parentheses.size() == 0;

    }

    // public boolean isValid(String s) {

    //     Stack<Character> parentheses = new Stack<>();
    //     // 맵으로 조건문 간소화
    //     Map<Character, Character> parenthesisMap = Map.of(')', '(', '}', '{', ']', '[');

    //     for (char c : s.toCharArray()) {
    //         if (parentheses.isEmpty()) {
    //             parentheses.push(c);
    //             continue;                
    //         }           
    //         if (parentheses.peek() == parenthesisMap.get(c)) {
    //             parentheses.pop();
    //         } else {
    //             parentheses.push(c);
    //         }
    //     }

    //     return parentheses.size() == 0;

    // }

    // public boolean isValid(String s) {

    //     Stack<Character> parentheses = new Stack<>();

    //     for (char c : s.toCharArray()) {
    //         if (parentheses.isEmpty()) {
    //             parentheses.push(c);
    //             continue;                
    //         }               
    //         if ((parentheses.peek() == '(' && c == ')') ||
    //             (parentheses.peek() == '{' && c == '}') ||
    //             (parentheses.peek() == '[' && c == ']')) {            
    //             parentheses.pop();
    //         } else {
    //             parentheses.push(c);
    //         }
    //     }

    //     return parentheses.size() == 0;

    // }
}

