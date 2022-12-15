/* 
LeetCode 13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Constraints:
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].
*/

#include <array>
#include <iostream>
#include <string>

using namespace std;

const array<string, 13> symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

const array<int, 13> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

class Solution {
public:
    int romanToInt(string const& s) const {
        int result = 0;
        int i = 0;
        for (int k = 0; k < symbols.size(); k++) {
            if (i == s.length()) {
                break;
            }
            if (symbols[k].length() == 1) {
                while (i < s.length() && s[i] == symbols[k][0]) {
                    i += 1;
                    result += values[k];
                }
            } 
            else if (symbols[k].length() == 2) {
                while (i + 1 < s.length() && s[i] == symbols[k][0] && s[i+1] == symbols[k][1]) {
                    i += 2;
                    result += values[k];
                }
            }
        }
        return result;
    }
};

int main() {
    Solution solution;
    cout << "Solution: " << solution.romanToInt("VIII") << "\n";
    return 0;
}
