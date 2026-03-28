/*
// 첫번째 풀이, 
// int -> string -> bit -> length
// 형변환을 하지 않고 하는 방법 필요
class Solution {
    public int hammingWeight(int n) {
        String intConvertBit = String.format("%32s", Integer.toBinaryString(n)).replaceAll(" ", "0");

        return intConvertBit.replaceAll("0", "").length();
    }
}

// 32비트로 굳이 변환할 필요가 없는데..?
// 음수는 안들어오니, 비트 변환 후 바로 체크하여 반환
class Solution {
    public int hammingWeight(int n) {
        return Integer.toBinaryString(n).replaceAll("0", "").length();
    }
}

// 두번째 풀이,
// length말고 counting으로?
class Solution {
    public int hammingWeight(int n) {
        String s = Integer.toBinaryString(n);

        int count = 0;
        for (char c: s.toCharArray()) {
            if (c == '1') count++;
        }

        return count;
    }
}

// 세번째 풀이
// int형 그대로 사용(달레님 강의 참고하여 풀이)
// 10진수를 0이 될 때까지 계속 2로 나누고 나머지를 모두 연결한다.
class Solution {
    public int hammingWeight(int n) {
        int cnt = 0;
        while (n > 0) {
            cnt += n % 2;
            n = n /2;
        }
        return cnt;
    }
}
 */

// 네번째 풀이
// 비트 조작을 통한 풀이
// 마지막 비트가 1인지 확인 
//  비트를 오른쪽으로 한 칸 이동시키고, 왼쪽 빈자리를 0으로 채움
class Solution {
    public int hammingWeight(int n) {
        int cnt = 0;
        while (n > 0) {
            cnt += (n & 1);
            n >>>= 1;
        }
        return cnt;
    }
}
