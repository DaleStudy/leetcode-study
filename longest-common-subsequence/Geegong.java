import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Geegong {

    /**
     * LIS, LCS 와 연관지어서 풀이
     * 1. 먼저 text1을 훑어보는데 text1에 중복되는 알파벳이 있을 수 있기에 각 캐릭터별로 인덱스들을 저장 (각 원소가 arrayList가 있는 배열)
     * 2. text2 를 훑으면서 매칭되는 캐릭터들에 대해서만 1에서 저장된 인덱스들을 한 배열안에 나열
     * -> 이떄 나열해서 넣을때마다 역순으로 집어넣는게 중요! (왜냐면 이 나열된 인덱스들을 가지고 LIS를 구할거라서)
     * 3. 나열된 인덱스들의 값들을 가지고 LIS 를 구한다, 즉 이 LIS의 길이가 LCS 의 길이가 된다..!! (와우 신기)
     * 그러나 leet code 에 돌렸을 때 runtime 이 영 좋지는 않음
     *
     * time complexity : O(M + N logN) => text2에 대해서 문자마다 바이너리서치가 수행됨
     * space complexity : O(M+N)
     * @param text1
     * @param text2
     * @return
     */
    public int longestCommonSubsequence(String text1, String text2) {

        /**
         * DP 를 이용한 LIS 구하기
         * 2차원 배열을 만들어 text1, text2 들을 하나씩 훑어가며
         * 이전에 일치했던 각 character 별로 횟수들을 기록해가며 더 LIS 로 붙일 수 있는지 정리해가는 기법
         * 참고 블로그 : https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence
         * time complexity : O(M * N) => O (N)
         * space complexity : O(M * N) => O (N)
         */
        char[] ch1 = text1.toCharArray();
        char[] ch2 = text2.toCharArray();

        int[][] LISArr = new int[ch1.length + 1][ch2.length + 1];

        // first, fill zeros in first row, first column for convenient
        for (int idx=0; idx<=ch2.length; idx++) {
            LISArr[0][idx] = 0;
        }

        for (int idx=0; idx<=ch1.length; idx++) {
            LISArr[idx][0] = 0;
        }

        int maxLIS = 0;
        for (int index1 = 0; index1<ch1.length; index1++) {
            for (int index2 = 0; index2<ch2.length; index2++) {

                // if same, then
                if (ch1[index1] == ch2[index2]) {
                    // LISArr 의 인덱스값이 +1 이 되는 이유는 LISArr 의 크기가 text1, text2 크기 + 1 만큼 만들었기 때문
                    LISArr[index1 + 1][index2 + 1] = LISArr[index1][index2] + 1;
                } else {
                    int biggerOne = Math.max(LISArr[index1][index2 + 1], LISArr[index1 + 1][index2]);
                    LISArr[index1 + 1][index2 + 1] = biggerOne;
                }

                maxLIS = Math.max(maxLIS, LISArr[index1 + 1][index2 + 1]);
            }
        }

        return maxLIS;



        /**
         * LIS, LCS 와 연관지어서 풀이
         * 1. 먼저 text1을 훑어보는데 text1에 중복되는 알파벳이 있을 수 있기에 각 캐릭터별로 인덱스들을 저장 (각 원소가 arrayList가 있는 배열)
         * 2. text2 를 훑으면서 매칭되는 캐릭터들에 대해서만 1에서 저장된 인덱스들을 한 배열안에 나열
         * -> 이떄 나열해서 넣을때마다 역순으로 집어넣는게 중요! (왜냐면 이 나열된 인덱스들을 가지고 LIS를 구할거라서)
         * 3. 나열된 인덱스들의 값들을 가지고 LIS 를 구한다, 즉 이 LIS의 길이가 LCS 의 길이가 된다..!! (와우 신기)
         * 그러나 leet code 에 돌렸을 때 runtime 이 영 좋지는 않음
         *
         * time complexity : O(M + N logN) => text2에 대해서 문자마다 바이너리서치가 수행됨
         * space complexity : O(M+N)
         */
//        char[] chText1 = text1.toCharArray();
//        char[] chText2 = text2.toCharArray();
//
//        // text1만 각 원소 별로 char가 가지는 index를 array 로 갖는 배열을 생성
//        List<Integer>[] positionIndices = new List[26];
//        for (int index = 0; index<chText1.length; index++) {
//            if (positionIndices[chText1[index] - 'a'] == null) {
//                positionIndices[chText1[index] - 'a'] = new ArrayList();
//                positionIndices[chText1[index] - 'a'].add(index);
//            } else {
//                positionIndices[chText1[index] - 'a'].add(index);
//            }
//        }
//
//
//        // 여기서부터 LIS 를 구할것임
//        List<Integer> indices = new ArrayList<>();
//        for (int index=0; index<chText2.length; index++) {
//
//            char find = chText2[index];
//            if (positionIndices[find-'a'] != null && positionIndices[find-'a'].size() > 0) {
//                // 역순 (LIS 를 구하기 위해서 일부러 뒤집어 높음, 즉 각 char 별 LIS 를 구할것이기 때문에..)
//                // positionIndices 에서 구했던 값들을 그대로 addAll 한다면 오름차순이 되기때문에 정확한 LIS 를 구할 수 없다
//
//                indices.addAll(positionIndices[find-'a'].stream().sorted(Comparator.reverseOrder()).toList());
//            }
//        }
//
//        // find LIS
//        return findLIS(indices).size();
    }

    public List<Integer> findLIS(List<Integer> source) {
        if (source.size() == 0) {
            return source;
        }

        List<Integer> LISResult = new ArrayList<>();
        for (int index=0; index<source.size(); index++) {
            int target = source.get(index);
            int insertionPosition = Collections.binarySearch(LISResult, target);
            //Returns:
            //the index of the search key, if it is contained in the list;
            // otherwise, (-(insertion point) - 1). The insertion point is defined as the point at which the key would be inserted into the list:
            if (insertionPosition < 0) {
                insertionPosition = -insertionPosition - 1;
            }

            if (LISResult.size() == insertionPosition) {
                LISResult.add(target);
            } else {
                LISResult.set(insertionPosition, target);
            }
        }

        return LISResult;
    }

}

