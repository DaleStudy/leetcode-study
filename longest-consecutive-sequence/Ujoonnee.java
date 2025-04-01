import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        // 중복 제거 후 오름차순 정렬
        Set<Integer> distinct = new HashSet<>();
        for (int num : nums) {
            distinct.add(num);
        }
        List<Integer> list = new ArrayList<>(distinct);
        Collections.sort(list);

        // 연속된 숫자라면 스택에 저장
        Stack<Integer> stack = new Stack<>();
        int answer = 0;
        for (int num : list) {
            if (stack.isEmpty()) {
                stack.add(num);
                continue;
            }

            // 연속된 숫자가 아니라면 현재까지 연속된 수를 저장 후 스택 초기화
            if (stack.peek() + 1 != num) {
                answer = Math.max(answer, stack.size());
                stack.clear();
            }

            stack.add(num);
        }

        return Math.max(answer, stack.size());
    }
}
