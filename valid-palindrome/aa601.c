bool isPalindrome(char* s) {
	int		i;
	int		j;
	int		size;
	char	tmp;
	int		flag;

	i = 0;
	size = strlen(s);
	j = size - 1;
	flag = 1;
	while (i < j) {
		if (!isalnum(s[i])) {
			++i;
			continue ;
		}
		else if (!isalnum(s[j])) {
			--j;
			continue ;
		}
		if (tolower(s[i++]) != tolower(s[j--])) {
			flag = 0;
			break ;
		}
	}
	return (flag);
}
