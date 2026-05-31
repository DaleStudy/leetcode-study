class Solution {
    public int maxArea(int[] height) {
        // 높이 순서대로 정렬해서, 처음부터 2개씩 잡아서 너비를 구하는 방법 => n^2
        // 해설 참고함. -> 포인터 2개를 둬서 양측에서 시작해서 중간에 만날때까지 최대값을 구한다
        int s = 0;
        int e = height.length - 1;
        int result = 0;

        while(s < e) {
            int h = height[s] < height[e] ?  height[s] :  height[e];
            int w = e - s;
            int cur = h * w;
            if (cur > result) {
                result = cur;
            }

            if (height[s] < height[e]) {
                s++;
            } else {
                e--;
            }
            // System.out.println(s + " " + e + " " + cur);
        }
        return result;
    }
}
