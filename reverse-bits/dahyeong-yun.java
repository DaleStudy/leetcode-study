/**
 * TC : O(1)
 *   - 32번의 루프를 2번 반복하므로 O(1)
 * SC : O(1)
 *   - 32칸 고정 길이의 stack이 필요하므로 O(1)
 */

class Solution {
    public int reverseBits(int n) {
        int answer = 0;
        Deque<Integer> stack = new ArrayDeque<>();

        for(int i = 0; i<32; i++) {
            stack.add(n % 2);
            n /= 2;
        }

        int j = 0;
        while(!stack.isEmpty()) {
            int bit = stack.getLast();
            stack.removeLast();
            answer += bit * Math.pow(2, j); 
            j += 1;
        }

        return answer;       
    }
}
