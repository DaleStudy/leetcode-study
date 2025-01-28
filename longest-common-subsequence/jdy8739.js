/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    const resultMap = new Map();

    const dfs = (i, j) => {
        const mapKey = `${i}-${j}`;

        if (resultMap.has(mapKey)) {
            return resultMap.get(mapKey);
        }

        if (i === text1.length || j === text2.length) {
            return 0;
        }

        if (text1[i] === text2[j]) {
            const resultHit = 1 + dfs(i + 1, j + 1);
            resultMap.set(mapKey, resultHit);
            return resultHit;
        }

        const resultMiss = Math.max(dfs(i + 1, j), dfs(i, j + 1));
        resultMap.set(mapKey, resultMiss);
        return resultMiss;
    }

    return dfs(0, 0);
};

// 시간복잡도 O(m * n) -> 재귀를 통해 m과 n이 1씩 증가하면서 상대편의 m or n 번 째 인덱스 문자열을 비교하므로??? (잘 모르겠습니다. 리뷰어분이 여유되시면 설명부탁드립니다 ㅜㅜ)
// 공간복잡도 O(m * n) -> 맵에 키가 m * n개로 최대로 요소가 들어옴
