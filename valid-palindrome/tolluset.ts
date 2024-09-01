/*
 * TC: O(n)
 * SC: O(n)
 * */
function isPalindrome(s: string): boolean {
  const parsedString = s.replace(/[^A-Za-z0-9]/g, "").toLowerCase();
  const n = parsedString.length;

  if (n === 0) {
    return true;
  }

  for (let i = 0; i < n / 2; i++) {
    if (parsedString[i] !== parsedString[n - i - 1]) {
      return false;
    }
  }

  return true;
}

// Time complexity: O(n)

const t1 = isPalindrome("A man, a plan, a canal: Panama");
console.info("🚀 : tolluset.ts:18: t1=", t1);

const t2 = isPalindrome("race a car");
console.info("🚀 : tolluset.ts:21: t2=", t2);

const t3 = isPalindrome(" ");
console.info("🚀 : tolluset.ts:24: t3=", t3);
