/**
 * 문자열을 알파벳 대문자를 소문자로 변환 및 숫자만 남기는 변환 유틸
 * - 시간 복잡도: O(n) (입력된 문자열의 길이에 비례)
 * 
 * @param {string} s - 정제할 물자열
 * @returns {string} - 소문자 알파벳과 숫자로 이루어진 문자열
 */
const refinePhrase = (s:string) : string => s.toLowerCase().replace(/[^a-z0-9]/g, '');


/**
 * 문자열을 정제후 palindrome 여부 확인 하는 함수
 * - 시간 복잡도: O(n) (문자열 정제 + 투 포인터 알고리즘)
 * 
 * @param {string} s palindrome 여부를 확인할 문자열
 * @returns {boolean} palindrome 여부
 */
function isPalindrome(s: string): boolean {
    const refined = refinePhrase(s);

    // two pointer를 활용한 palindrome 확인 O(n)
    let left = 0, right = refined.length - 1;
    while (left < right) {
        if (refined[left] !== refined[right]) {
            return false;
        }
        left++;
        right--;
    }

    return true;
}
