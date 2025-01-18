// 스택을 사용해 시간복잡도를 O(N)으로 풀어야하는 문제.
// toCharArray로 문자열을 자르는 시간을 대폭 줄일 수 있다. charAt도 그닥 좋은 방법은 아닌듯
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        if(s.length() == 1) return false;
        boolean valid = false;
        for(char c : s.toCharArray()) {
            valid = false;
            if(c == '(' || c == '{' || c == '[') {
                stack.push(c);
                continue;
            }

            if(!stack.isEmpty() && c == ')' && stack.peek() == '(') {
                valid = true;
                stack.pop();
                continue;
            }

            if(!stack.isEmpty() && c == '}' && stack.peek() == '{') {
                valid = true;
                stack.pop();
                continue;
            }

            if(!stack.isEmpty() && c == ']' && stack.peek() == '[') {
                valid = true;
                stack.pop();
                continue;
            }
            break;
        }

        if (!stack.isEmpty()) return false;

        return valid;
    }
}

// 첫 풀이. s.split("") 하나가 제법 많은 시간 복잡도를 사용한다.
// String 객체할당과 배열 재생성 등의 과정을 거친다. 그래서... 다른 방법을 찾아봄
class Solution {
    public boolean isValid(String s) {
        Stack<String> stack = new Stack<>();

        if(s.length() == 1) return false;
        boolean valid = false;
        for(String str : s.split("")) {
            valid = false;
            if(str.equals("(") || str.equals("{") || str.equals("[") ) {
                stack.push(str);
                continue;
            }

            if(!stack.isEmpty() && str.equals(")") && stack.peek().equals("(")) {
                valid = true;
                stack.pop();
                continue;
            }

            if(!stack.isEmpty() && str.equals("]") && stack.peek().equals("[")) {
                valid = true;
                stack.pop();
                continue;
            }

            if(!stack.isEmpty() && str.equals("}") && stack.peek().equals("{")) {
                valid = true;
                stack.pop();
                continue;
            }
            break;
        }
        
        if (!stack.isEmpty()) return false;

        return valid;
    }
}
