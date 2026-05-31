/*
s에서 알파벳과 숫자가 아닌 글자를 다 날리고, 스택에 문자를 절반까지 담은 후 절반 이후부터는 꺼내가며 앞뒤 레터가 일치하는지 확인한다

시간복잡도 : O(N) (N은 s의 길이)
공간복잡도 : O(N) (스택)
*/

function isPalindrome(s: string): boolean {
  const newStr = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase()
  const isStrEven = newStr.length % 2 === 0
  const lenHalf = Math.floor(newStr.length / 2)
  const stack = []
  for (let i = 0; i < newStr.length; i++) {
    if (i < lenHalf) {
      stack.push(newStr[i])
    } else {
      if (!isStrEven && i === lenHalf) continue
      const isSame = newStr[i] === stack.pop()
      if (!isSame) return false
    }
  }
  return true
}
