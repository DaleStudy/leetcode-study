class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> count = new HashMap<>();
        int left = 0;
        int answer = 0;
        int size = 0;

        for (int right = 0; right < s.length(); right++) {
            // 1) right 문자를 윈도우에 넣는다
            count.merge(s.charAt(right), 1, Integer::sum);
            size ++;
            // 2) 윈도우가 조건을 어기는 동안 left를 오른쪽으로 민다
            int maxCount = Collections.max(count.values());
            while ( size - maxCount  > k ) {
                count.merge(s.charAt(left), -1, Integer::sum);
                size --;
                left++;
            }

            // 3) 지금 윈도우는 유효하니까 답 갱신
            answer = Math.max(answer,size);
        }

        return answer;
    }
}
