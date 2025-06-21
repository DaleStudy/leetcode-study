
// tc -> O(1) 
// NOTE: 자바의 Integer.parseInt는 음수 표현을 처리하지 못함.. 양의 부호가 없는 이진수만 지원. (음수의 경우 1111111~ 로 시작하는 이진 문자열을 양수로 해석하려 시도해 런타임 오류 발생)
class Solution {
    public int getSum(int a, int b) {
        String aStr = String.format("%32s", Integer.toBinaryString(a)).replace(" ", "0");
        String bStr = String.format("%32s", Integer.toBinaryString(b)).replace(" ", "0");
        char[] sum = new char[32];
        boolean isCarry = false;

        for (int i = sum.length - 1; i >= 0; i--) {
            if (aStr.charAt(i) == bStr.charAt(i) && aStr.charAt(i) == '1') {

                sum[i] = isCarry ? '1' : '0';
                isCarry = true;
                continue;
            }

            if (aStr.charAt(i) == '1' || bStr.charAt(i) == '1') {
                sum[i] = isCarry ? '0' : '1';
                isCarry = isCarry ? true : false;
                continue;
            }

            sum[i] = isCarry ? '1' : '0';
            isCarry = false;
        }

        String resStr = new String(sum);
        return (int) Long.parseLong(resStr, 2);
    }
}
