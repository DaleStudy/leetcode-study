/**
 * palindrom: 회문, 거꾸로 읽어도 제대로 읽는 것과 같은 문장
 * @param s
 */
function isPalindrome(s: string): boolean {
    let word = s.toLowerCase();
    const reg = /[^a-z0-9]/g; // removing all non-alphanumeric characters
    word = word.replace(reg, '');

    for(let i = 0; i < word.length; i++) {
        if(word[i] !== word[word.length-i-1])
            return false;
    }
    return true;
};
