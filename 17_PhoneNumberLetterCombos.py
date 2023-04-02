"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Constraints: 
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

class Solution:
	lettersForDigit = {
		"2": "abc", "3": "def",  "4": "ghi", "5": "jkl", 
		"6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
	}
	def letterCombinations(self, digits: str) -> list[str]:
		if len(digits) == 0:
			return []
		solution = [""]
		for currentDigit in digits:
			currentLetters = self.lettersForDigit[currentDigit]
			currentSolution = []
			for string in solution:
				for letter in currentLetters:
					currentSolution.append(string + letter)
			solution = currentSolution
		return solution
	
s = Solution()
print(s.letterCombinations("2"))
print()
print(s.letterCombinations("23"))
print()
print(s.letterCombinations("47"))