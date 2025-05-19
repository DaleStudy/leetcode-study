// tc: O(n)
// 투 포인터라는 문제풀이 방법으로 간단히 (답지보고) 해결...
class Solution { 
    public int maxArea(int[] h) {
        int start = 0;
        int end = h.length - 1;
        int mx = -987654321;
        
        while(start < end) {
            mx = Math.max(mx, (end - start) * Math.min(h[start], h[end]));

            if(h[start] < h[end])   {
                start++;
            } else {
                end--;
            }
        }
        
        return mx;
    }
}


// 예외처리가 덕지덕지 붙기 시작할 때. (잘못됨을 깨닫고)다른 방법으로 풀어햐 하는건 아닌지 생각하는 습관 필요함..ㅠ
class WrongSolution {
    public int maxArea(int[] h) {
        int mx = Math.min(h[0], h[1]);
        int idx = 0;

        for(int i = 1; i < h.length; i++) {
            int offset = i - idx;
            
            int prevCalc = Math.min(h[i - 1], h[i]);
            int calc = Math.min(h[idx], h[i]);
            int newMx = calc * offset;

            // 새롭게 인덱스를 바꿔버리는게 더 나을때.
            if(prevCalc > newMx) {
                idx = i - 1;
                mx = Math.max(mx, prevCalc);
                continue;
            }

            // 물을 더 많이 담을 수 있을 때.
            if(h[idx] < h[i] && newMx > mx) {
                if(i == 2) {
                   int exc = Math.min(h[1], h[i]) * offset;
                   if(exc > newMx) {
                    idx = 1;
                    mx = Math.max(exc, mx);
                    continue;
                   }
                }
                
                idx = i;
            }

            mx = Math.max(newMx, mx);
        }

        return mx;
    }
}
