import java.util.HashMap;
import java.util.Map;

// NOTE: sliding window　방식으로 풀이했던 답지... 아직 if　구문이나, 반환값의 이유가 이해되지 않았다. 별도로 정리 + 한번 더 풀어보기.
// TC -> O(n)
class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> cMap = new HashMap<>();

        int mx = 0;
        int left = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            cMap.put(c, cMap.getOrDefault(c, 0) + 1);

            mx = Math.max(mx, cMap.get(c));

            if (i - left + 1 - mx > k) {
                cMap.put(s.charAt(left), cMap.getOrDefault(s.charAt(left), 0) - 1);
                left++;
            }
        }

        return s.length() - left;
    }
}

// NOTE: 구현에 시간이 너무 오래걸려 일단 스킵.. (현재 알고리즘에서 최대 연속되는 빈도들의 후보군들을 정하고, 그 후보군들만
// 치환해보는 방식을 사용해도 될 것 같다...)
class WrongSolution {
    public int characterReplacement(String s, int k) {

        if (s.length() == k) {
            return k;
        }

        // ward: 가장 많은 빈도수의 문자와 인덱스가 정확하게 나오지 않는 이슈가 있다.
        int mx = 1;
        int gMx = 1;
        int index = 0;
        char prev = s.charAt(0);
        for (int i = 1; i < s.length(); i++) {
            char cur = s.charAt(i);

            if (prev == cur) {
                mx++;
            } else {
                // System.out.println("mx " + mx);
                // System.out.println("gMx " + gMx);
                if (mx > gMx) {
                    // System.out.println(i - 1);
                    gMx = mx;
                    index = i - 1;
                }

                mx = 1;
                prev = cur;
            }
        }

        if (mx > gMx) {
            gMx = mx;
            index = s.length() - 1;
        }

        // k번 오른쪽으로 이동하며 가장 큰 문자를 치환.
        char mostFreq = s.charAt(index);
        char[] cArrR = s.toCharArray();
        char[] cArrL = s.toCharArray();

        int cnt = 0;
        int init = 1;
        // System.out.println("index " + index);
        // System.out.println("mostFreq " + mostFreq);
        while (cnt <= k - 1) {
            int targetIndex = index + init;

            // System.out.println("called " + targetIndex);

            if (targetIndex >= s.length()) {
                break;
            }

            if (cArrR[targetIndex] == mostFreq) {
                init++;
                continue;
            }

            cArrR[targetIndex] = mostFreq;
            init++;
            cnt++;
        }

        for (char anChar : cArrR) {
            System.out.print(anChar);
        }
        System.out.println();

        if (cnt < k) {
            int startIndex = index - mx; // 맞느지 직접 확인해봐야함.
            int temp = 1;
            while (cnt <= k - 1) {
                int targetIndex = startIndex - temp;

                if (targetIndex < 0) {
                    break;
                }

                if (cArrR[targetIndex] == mostFreq) {
                    temp++;
                    continue;
                }

                cArrR[targetIndex] = mostFreq;
                temp++;
                cnt++;
            }
        }

        // 위에서 사용한 cnt 변수 초기화
        cnt = 0;
        init = 1;
        if (index != 0) {
            // k번 왼쪽으로 이동하며 가장 빈도높게 나왔던 문자를 치환.
            while (cnt <= k - 1) {
                int targetIndex = index - init;

                if (targetIndex < 0) {
                    break;
                }

                if (cArrL[targetIndex] == mostFreq) {
                    init++;
                    continue;
                }

                cArrL[targetIndex] = mostFreq;
                init++;
                cnt++;
            }
        }

        if (cnt < k) {
            int temp = 1;
            while (cnt <= k - 1) {
                int targetIndex = temp + index;

                if (targetIndex >= s.length()) {
                    break;
                }

                if (cArrL[targetIndex] == mostFreq) {
                    temp++;
                    continue;
                }

                cArrL[targetIndex] = mostFreq;
                temp++;
                cnt++;
            }
        }

        for (char anChar : cArrL) {
            System.out.print(anChar);
        }
        System.out.println();

        // 왼쪽 오른쪽으로 치환된 문자열들에 대해서 각각 가장 연속된 문자열 길이 구하는 동작 수행하기
        int gMxR = 1;
        int gMxL = 1;
        int mxR = 1;
        int mxL = 1;
        int prevR = cArrR[0];
        int prevL = cArrL[0];
        for (int i = 1; i < s.length(); i++) {
            char curR = cArrR[i];
            char curL = cArrL[i];

            if (prevR == curR) {
                mxR++;
            } else {
                gMxR = Math.max(gMxR, mxR);
                mxR = 1;
                prevR = curR;
            }

            if (prevL == curL) {
                mxL++;
            } else {
                gMxL = Math.max(gMxL, mxL);
                mxL = 1;
                prevL = curL;
            }
        }

        gMxR = Math.max(mxR, gMxR);
        gMxL = Math.max(mxL, gMxL);

        return Math.max(gMxR, gMxL);
    }
}
