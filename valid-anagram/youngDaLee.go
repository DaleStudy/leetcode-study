package youngDaLee

import "strings"

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	if s == t {
		return true
	}

	sDict := make(map[string]int)
	sList := strings.Split(s, "")
	for _, data := range sList {
		if num, ok := sDict[data]; ok {
			sDict[data] = num + 1
		} else {
			sDict[data] = 1
		}
	}

	tList := strings.Split(t, "")
	for _, data := range tList {
		if num, ok := sDict[data]; ok {
			sDict[data] = num - 1
		} else {
			return false
		}

		if sDict[data] < 0 {
			return false
		}
	}

	for _, num := range sDict {
		if num != 0 {
			return false
		}
	}

	return true
}
