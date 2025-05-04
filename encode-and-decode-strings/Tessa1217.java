/**
 * 문자열에 대한 encode, decode 알고리즘 디자인
 * 문자열은 ASCII 256 모두 포함 가능 (문자만 포함한 게 아니므로 특수문자(:, ?) 등도 알고리즘 내에서 고려해야 함
 * */

import java.util.ArrayList;
import java.util.List;

public class Solution {

    public static String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String str : strs) {
            // : 구분자 앞에 단어의 길이 추가
            sb.append(str.length()).append(":").append(str);
        }
        return sb.toString();
    }

    public static List<String> decode(String str) {
        List<String> words = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            // 구분자 기준 인덱스
            int colonIdx = str.indexOf(':', i);
            // 단어의 길이 인덱스
            int length = Integer.parseInt(str.substring(i, colonIdx));
            // 단어 시작
            int wordStart = colonIdx + 1;
            // 단어의 끝
            int wordEnd = wordStart + length;
            words.add(str.substring(wordStart, wordEnd));
            i = wordEnd;
        }
        return words;
    }

}

