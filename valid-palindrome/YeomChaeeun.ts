/**
 * palindrom: 회문, 거꾸로 읽어도 제대로 읽는 것과 같은 문장
 * @param s
 */
function isPalindrome(s: string): boolean {
    let word = s.toLowerCase();
    const reg = /[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\" ]/g;

    word = word.replace(reg, '');
    for(let i = 0; i < word.length; i++) {
        for(let j = word.length-i-1; j >= word.length-i-1; j--) {
            // console.log(word[i], '===', word[j])
            if(word[i] !== word[j]) return false;
        }
    }
    return true;
};
