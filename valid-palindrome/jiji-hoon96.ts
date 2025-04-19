/**
 *
 * @param s
 *
 * 풀이 1
 *
 * 특수문자 정규 표현식이 복잡하고, 분할과 합치는 과정이 중복된다
 *
 * function isPalindrome(s: string): boolean {
 *     const reg= /[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]/gi;
 *     let palindrome= s.replace(reg,'').toLowerCase().split('');
 *
 *     return palindrome.join('').replace(/ /g,"")===palindrome.reverse().join('').replace(/ /g,"")
 * };
 *
 * 그래서 생각한 풀이 2는 s consists only of printable ASCII characters. 을 보고 숫자와 알파벳을 제외하고 나머지는 제거하고
 * 투포인트 방법으로 변경해서 문제 해결
 */

function isPalindrome(s: string): boolean {
    const cleanStr = s.toLowerCase().replace(/[^a-z0-9]/g, '');

    let left = 0;
    let right = cleanStr.length-1;

    while(left < right){
        if(cleanStr[left] !== cleanStr[right]){
            return false;
        }
        left++;
        right--;
    }
    return true
};
