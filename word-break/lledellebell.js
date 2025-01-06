/**
 * @problem
 * 주어진 문자열 s가 단어 사전 wordDict에 포함된 단어들로만 구성될 수 있는지 확인하는 문제입니다.
 * 단어 사전의 단어들은 여러 번 사용할 수 있으며, 문자열 s를 완전히 나눌 수 있어야 합니다.
 *
 * @constraints
 * - 1 <= s.length <= 300
 * - 1 <= wordDict.length <= 1000
 * - 1 <= wordDict[i].length <= 20
 * - s와 wordDict[i]는 모두 소문자 알파벳으로만 구성됩니다.
 * 
 * @param {string} s - 주어진 문자열
 * @param {string[]} wordDict - 단어 사전
 * @returns {boolean} 문자열 s가 단어 사전의 단어들로만 나눌 수 있는지 여부
 *
 * @example
 * - 예제 1:
 *   ㄴ Input: s = "leetcode", wordDict = ["leet", "code"]
 *   ㄴ Output: true
 *   ㄴ Explanation: "leetcode"는 "leet" + "code"로 나눌 수 있습니다.
 * - 예제 2:
 *   ㄴ Input: s = "applepenapple", wordDict = ["apple", "pen"]
 *   ㄴ Output: true
 *   ㄴ Explanation: "applepenapple"는 "apple" + "pen" + "apple"로 나눌 수 있습니다.
 * - 예제 3:
 *   ㄴ Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
 *   ㄴ Output: false
 *   ㄴ Explanation: "catsandog"는 wordDict의 단어들로 나눌 수 없습니다.
 * 
 * @description
 * - 시간 복잡도: O(n^2)
 *   ㄴ 외부 반복문: 문자열 s의 길이 n에 대해 1부터 n까지 반복 (O(n))
 *   ㄴ 내부 반복문: 각 i에 대해 최대 i번 반복 (O(n))
 *   ㄴ substring 및 Set 검색: O(1) (substring은 내부적으로 O(k)이지만, k는 최대 단어 길이로 간주)
 *   ㄴ 결과적으로 O(n^2)의 시간 복잡도를 가짐
 * - 공간 복잡도: O(n + m)
 *   ㄴ dp 배열의 크기: s의 길이 n + 1 (O(n))
 *   ㄴ wordSet: wordDict의 단어 개수에 비례 (O(m), m은 wordDict의 단어 수)
 */
function wordBreak(s, wordDict) {
    // wordDict를 Set으로 변환하여 검색 속도를 O(1)로 만듦
    const wordSet = new Set(wordDict);

    // dp 배열 생성: dp[i]는 s의 처음부터 i번째 문자까지가 wordDict의 단어들로 나눌 수 있는지를 나타냄
    const dp = new Array(s.length + 1).fill(false);
    dp[0] = true; // 빈 문자열은 항상 나눌 수 있음

    // i는 문자열의 끝 인덱스를 나타냄
    for (let i = 1; i <= s.length; i++) {
        // j는 문자열의 시작 인덱스를 나타냄
        for (let j = 0; j < i; j++) {
            // dp[j]가 true이고, s[j:i]가 wordSet에 포함되어 있다면
            if (dp[j] && wordSet.has(s.substring(j, i))) {
                dp[i] = true; // dp[i]를 true로 설정
                break; // 더 이상 확인할 필요 없음
            }
        }
    }

    // dp[s.length]가 true라면 문자열 s를 wordDict의 단어들로 나눌 수 있음
    return dp[s.length];
}

const s1 = "leetcode";
const wordDict1 = ["leet", "code"];
console.log(wordBreak(s1, wordDict1)); // true

const s2 = "applepenapple";
const wordDict2 = ["apple", "pen"];
console.log(wordBreak(s2, wordDict2)); // true

const s3 = "catsandog";
const wordDict3 = ["cats", "dog", "sand", "and", "cat"];
console.log(wordBreak(s3, wordDict3)); // false
