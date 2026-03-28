function isPalindrome(s: string): boolean {
	const word = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
	if (word.length === 0) {
		return true;
	}

	for (let i = word.length - 1; i >= 0; i--) {
		if (word[i] !== word[word.length - 1 - i]) {
			return false;
		}
	}

	return true;
}

isPalindrome("A man, a plan, a canal: Panama"); // true
isPalindrome("race a car"); // false
isPalindrome(" "); // true
isPalindrome("0P"); // false
isPalindrome("a"); // true
