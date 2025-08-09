import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Geegong {

    /**
     * case 1. decodeMap 에 array 의 각 index 별로 디코딩이 가능한 자릿수를 list 로 관리
     * 후에 decodeMap 을 dfs 로 순회하면서 조합이 가능한 방법을 찾는 방법
     * 그러나 Time Limit Exceeded 발생ㅠㅠ
     * @param s
     * @return
     */
    public int numDecodings(String s) {
        Map<Integer, List<Integer>> decodeMap = new HashMap<>();
        char[] charArr = s.toCharArray();

        int prevVal = -1;
        for (int index=0; index<charArr.length; index++) {
            String str = String.valueOf(charArr[index]);
            int currentVal = Integer.valueOf(str);

            if (currentVal == 0 && (prevVal == -1 || prevVal > 2)) {
                // ex) 02xxxx.. , 30xxxx, 1230xxx, 1302xxx
                // there is no way
                return 0;
            } else if (currentVal == 0 && prevVal < 3 && prevVal > 0) {
                appendDigitNumbers(decodeMap, index - 1, 2, true);
            } else if (currentVal > 0) {
                appendDigitNumbers(decodeMap, index, 1, false);

                if (prevVal == 2 && currentVal < 7) {
                    // for maximum 26
                    appendDigitNumbers(decodeMap, index - 1, 2, false);
                } else if (prevVal > 0 && prevVal < 2) {
                    appendDigitNumbers(decodeMap, index - 1, 2, false);
                }

            }

            prevVal = currentVal;
        }


        // judge ways
        return dfs(decodeMap, 0);

    }

    public int dfs(Map<Integer, List<Integer>> decodeMap, int index) {
        // 자릿수 끝이면 끝
        if (index > decodeMap.keySet().size() - 1) {
            return 1;
        }

        int totalWays = 0;
        if (decodeMap.containsKey(index)) {
            List<Integer> waysDigitNumbers = decodeMap.get(index);

            for (Integer digit : waysDigitNumbers) {
                totalWays += dfs(decodeMap, index + digit);
            }
        }

        return totalWays;
    }

    public void appendDigitNumbers(Map<Integer, List<Integer>> decodeMap, int index, int digitNumber, boolean forceNewWays) {
        if (!decodeMap.containsKey(index) || forceNewWays) {
            List<Integer> waysDigitNumber = new ArrayList<>();
            waysDigitNumber.add(digitNumber);
            decodeMap.put(index, waysDigitNumber);
        } else {
            List<Integer> waysDigitNumber = decodeMap.get(index);
            waysDigitNumber.add(digitNumber);
            decodeMap.put(index, waysDigitNumber);
        }
    }
    
}
