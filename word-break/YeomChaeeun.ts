/**
 * 주어진 단어가 wordDict에 있는 단어들로 분할 가능한지 확인하기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(nmk) => 문자열 s의 길이 * wordDict 단어 개수 * wordDict 내 가장 긴 단어의 길이
 * - 공간 복잡도: O(n)
 * @param s
 * @param wordDict
 */
function wordBreak(s: string, wordDict: string[]): boolean {
    // 접근 1 - 단어 포함 여부만 고려하고 여러번 사용될 있고 연속성 검사를 하지 않았음
    // let len = 0;
    // for(const word of wordDict) {
    //     len += word.length
    //     if(!s.includes(word)) return false
    // }
    // if(s.length < len) return false
    // return true

    /* 해당 케이스에서 에러 발생함
    *  - 단어가 여러번 사용될 수 있기 때문
    *  s="bb"
    *  wordDict = ["a","b","bbb","bbbb"]
    */

    // 접근 2- dp 알고리즘 적용
    // 각 위치까지의 문자열이 분할 가능한지 저장함
    let dp: boolean[] = new Array(s.length).fill(false)

    for (let i = 0; i < s.length; i++) {
        for (let word of wordDict) {
            // 조건 처리 - 현재 위치가 단어 길이보다 작으면 스킵함
            if (i < word.length - 1) {
                continue
            }
            // 현재 위치의 유효성 체크 - 첫번째 단어이거나 이전 위치까지 분할 가능한지
            if (i == word.length - 1 || dp[i - word.length]) {
                // 현재 위치의 단어 매칭 체크
                if (s.substring(i - word.length + 1, i + 1) == word) {
                    dp[i] = true
                    break
                }
            }
        }
    }
    return dp[s.length - 1]
}
