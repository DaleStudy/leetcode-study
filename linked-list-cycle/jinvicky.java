import java.util.HashSet;
import java.util.Set;

public class Solution {
    /**
     * 문제에서 말하는 pos는 설명을 돕는 사이클 발생 위치이지 코드 상에서 사용하지 않는다.
     */
    public boolean hasCycle(ListNode head) {
        Set<Integer> set = new HashSet<>();
        while(head != null) {
            // set에서 이미 존재하는 숫자가 있으면 바로 return true;
            // set.add() 메서드는 추가 성공 시 true, 이미 존재하는 숫자면 추가하지 못하고 false를 반환한다.
            if(!set.add(head.val)) return true;
            head = head.next;
        }
        return false;
    }
}