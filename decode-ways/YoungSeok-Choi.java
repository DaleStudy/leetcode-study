
// NOTE: O(n)
class Solution {
    public int numDecodings(String s) {
        
        char[] cArr = s.toCharArray();
        int[] decode = new int[cArr.length];

        if((cArr[0] - 48) == 0) {
            return 0;
        }
        
        decode[0] = 1;

        for(int i = 1; i < cArr.length; i++) {
            int cur = (int) cArr[i] - 48;
            int prev = (int) cArr[i - 1] - 48;

            if(cur == prev && cur == 0) return 0;

            String temp = "" + cArr[i - 1] + cArr[i];
            int tempI = Integer.parseInt(temp);

            // NOTE: 아래 if 문 두개가 core logic
            if(cur != 0) {
                decode[i] += decode[i - 1];
            }

            if(tempI >= 10 && tempI <= 26) {
                decode[i] += (i >= 2 ? decode[i - 2] : 1);
            }
        }

        return decode[decode.length - 1];
    }
}


class WrongSolution {
    public int numDecodings(String s) {
        
        char[] cArr = s.toCharArray();
        int[] decode = new int[cArr.length];

        if((cArr[0] - 48) == 0) {
            return 0;
        }
        
        decode[0] = 1;

        // 유효한 경우만 판단해서 처리해주면 됐었던 문제.. 
        // 어떻게 처리해야할지 모르겠는 분기는 처리하지 않하느니만 못하다...ㅜ
        for(int i = 1; i < cArr.length; i++) {
            int cur = (int) cArr[i] - 48;
            int prev = (int) cArr[i - 1] - 48;

            if(cur == prev && cur == 0) return 0;

            String temp = "" + cArr[i - 1] + cArr[i];
            int tempI = Integer.parseInt(temp);

            if(cur >= 1 && cur <= 9) {
                decode[i] = decode[i - 1];

                if(prev >= 1 && prev <= 9) {
                    if(tempI >= 1 && tempI <= 26) {
                        decode[i] = i == 1 ? decode[i - 1] + 1 : decode[i - 1] + decode[i - 2];
                    }  
                } else { // 이전값이 0이라 정상적인 디코딩이 안되는 경우..
                    decode[i]--;
                }

            }  else { // 뒷 숫자와 합쳐져서 유효하게 될 수도 있는경우
                decode[i] = (tempI >= 1 && tempI <= 26) ? decode[i - 1] : 0;  
            }
        }

        return decode[decode.length - 1];
    }
}
