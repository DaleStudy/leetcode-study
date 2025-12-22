import java.util.Stack;

class Solution {
  /**
   * 1. 열기는 같은 타입의 닫기가 필요함.
   * 2. 열기는 정확한 순서로 닫기가 필요함.
   * 3. 모든 닫기 괄호는 열기 괄호에 대응됨..!
   * 
   * 스택을 이용하기
   * 1. 열기괄호를 스택에 넣기
   * 2. 닫기괄호를 보면 스택의 상단을 보기
   * > 상단과 닫기 괄호가 다르면? false
   * > 같으면 상단을 pop
   * 3. 맨 마지막에 스택은 비어있어야함.
   */
  public boolean isValid(String s) {
    char[] brkts = { '(', ')', '{', '}', '[', ']' };

    Stack<Integer> st = new Stack<>();
    // System.out.println("j->");
    for (int i = 0; i < s.length(); i++) {
      for (int j = 0; j < 6; j++) {
        // System.out.println("ㅑ->"+s.charAt(i)+" j->"+brkts[j]);
        if (s.charAt(i) == brkts[j]) {
          // 열기면 스택에 넣기
          if (j % 2 == 0) {
            st.push(j);
            // System.out.println("j->"+j);
          } else { // 닫기면 top이랑 비교하기
            // 스택이 비어있으면 false;
            if (st.size() == 0) {
              return false;
            }
            int top = st.pop();
            // System.out.println("j->"+j+" top->"+top+" remn_size->"+st.size());
            if (top + 1 != j) {
              // 상단값이 닫기 괄호랑 맞지 않으면 false
              return false;
            }
          }
        }
      }
    }
    // 스택에 괄호가 남아있으면 false
    if (st.size() > 0) {
      return false;
    }
    return true;
  }
}
