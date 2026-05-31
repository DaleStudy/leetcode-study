/*
1. 문제 이해

입력으로 string s 와 int k 가 있고 s 에 대해 k번 만큼 글자를 바꿀 수 있다.
이때 최대로 연속된 substring의 길이를 찾는 것이다.
즉 k번만큼 바꿀 때 최대의 substring이 될 수 있도록 글자를 바꿔야 한다.

조건: s길이는 최대 10만, k는 최대 s길이

여기서 한가지 포인트는 전체 길이 n 에서 가장 긴 동일 문자 길이 s 를 뺀 값인 n - s 가 k보다 작거나 같다면 이건 항상 전체 길이 만큼에 대해 동일 문자열로 변경할 수 있는것을 의미한다.
왜냐하면 바꿔야할 문자 개수보다 바꿀 수 있는 개수가 더 많기 때문이다.

2. 알고리즘

substring인걸 보니 다이나믹 프로그래밍이 생각나는데 어떻게 적용시켜야할지 고민이다.
작은 문제를 어떻게 정의해야할까 ?

만약 dp가 아니라면?

정답 참고 -> 슬라이딩 윈도우 기법을 사용한다
2개의 포인터를 동일한 인덱스에 놓고 종료 인덱스를 1칸씩 늘려가면서 다른 문자열이 나오는지 체킹한다

3. 예외


4. 구현

GPT 참고

이걸 구현 하는 부분에서 특히 while문을 이해하기 어려웠다.

for문을 통해 end 포인터를 하나씩 증가시킨다
이를 통해 윈도우 크기를 증가시킨다
그리고 counter map에 해당 글자 count를 1 추가하여 넣는다
모든 글자 count들을 돌면서 최대 maxCount를 찾는다

그리고 중요한 조건인 k번을 사용해서 현재 윈도우를 동일한 글자로 만들 수 있는지 찾아낸다.
이때 while문의 (end - start + 1 - maxCount > k) 부분이 핵심이다. 가장 위에서 설명한 대로 현재 윈도우 길이 + 1 - maxCount 가 k보다 크다는 것은 변경해야할 길이가 변경할 수 있는 길이보다 크다는 것이므로 모두 동일한 글자로 만들 수 없다는 것이므로 윈도우 크기를 왼쪽에서 줄여나가야 한다.

이렇게 줄여나가다가 변경해야할 길이 = 변경할 수 있는 길이 가 되면 현재 start ~ end 윈도우에서 가질 수 있는 최대의 동일 글자 길이 조건을 만족시키므로 maxLen를 초기화 시켜준다.

현재 start ~ end 에서 최대 길이를 알아냈으므로 그 다음 end를 증가시키며 이 과정을 반복한다.


GPT 면접식 답변

🎤 ① 문제 핵심 정의부터 말한다

“이 문제의 핵심은
연속된 부분 문자열을 하나 선택했을 때,
최대 k번 문자 교체로 모두 같은 문자로 만들 수 있는지를 판단하는 것입니다.”

🎤 ② 판단 기준을 먼저 제시한다 (중요)

“어떤 부분 문자열의 길이를 n,
그 안에서 가장 많이 등장한 문자의 개수를 s라고 하면,
n - s ≤ k 인 경우에만
이 문자열은 k번 이내의 교체로 하나의 문자로 만들 수 있습니다.”

👉 여기서 면접관은 이미 ‘아, 본질 이해했구나’ 하고 체크함.

🎤 ③ 이 기준을 어떻게 효율적으로 찾는지 설명

“이 조건을 만족하는 가장 긴 n을 찾기 위해
저는 슬라이딩 윈도우를 사용했습니다.”

“오른쪽 포인터를 이동시키며 윈도우를 확장하고,
현재 윈도우 내 문자 빈도를 카운트합니다.”

🎤 ④ 윈도우 유지 조건 설명 (핵심 로직)

“현재 윈도우에서
(윈도우 길이 - 가장 많이 등장한 문자 수)가
k를 초과하면,
해당 구간은 더 이상 유효하지 않으므로
왼쪽 포인터를 이동시켜 윈도우를 줄입니다.”

👉 이 문장이 바로 코드의 while 조건 설명이다.

🎤 ⑤ 정답 갱신 시점 설명

“조건을 만족하는 동안에는
현재 윈도우 길이를 최대값으로 갱신하며
전체 탐색은 한 번만 이루어지므로
시간 복잡도는 O(N)입니다.”

*/

import java.util.*;

class Solution {
    public int characterReplacement(String s, int k) {
        int maxLen = 0;
        Map<Character, Integer> counter = new HashMap<>();

        int start = 0;

        for (int end = 0; end < s.length(); end++) {
            char c = s.charAt(end);
            counter.put(c, counter.getOrDefault(c, 0) + 1);

            int maxCount = 0;
            for (int count : counter.values()) {
                maxCount = Math.max(maxCount, count);
            }

            while (end - start + 1 - maxCount > k) {
                char leftChar = s.charAt(start);
                counter.put(leftChar, counter.get(leftChar) - 1);
                start++;
            }

            maxLen = Math.max(maxLen, end - start + 1);
        }

        return maxLen;
    }
}
