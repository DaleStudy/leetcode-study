/**
 * 주어진 배열의 원소 조합(중복 허용)의 합이 target인 모든 경우를 반환하는 함수
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
const combinationSum = function(candidates, target) {
    const sortedCandidates = candidates.filter((x) => x <= target).sort((a, b) => Number(a) - Number(b));
    const answer = [];
    
    if (sortedCandidates.length === 0) {
        return answer;
    }

    function search(currentIdx, combination, total) {
        if (total === target) {
            answer.push([...combination]); // 배열 자체를 넣으면 참조 때문에 값이 변경되므로, 복사해서 넣어야 함
            return;
        }

        if (total > target) {
            return; // backtracking
        }

        combination.push(sortedCandidates[currentIdx]);
        search(currentIdx, combination, total + sortedCandidates[currentIdx]);
        combination.pop();

        if (total + sortedCandidates[currentIdx] > target) {
            return; // backtracking
        }

        if (currentIdx + 1 < sortedCandidates.length) {
            search(currentIdx + 1, combination, total);
        }
    }

    search(0, [], 0);
    return answer;
};

// t: target
// 시간복잡도: O(2^t)
// 공간복잡도: O(t)
