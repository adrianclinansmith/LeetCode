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
#include <unordered_map>

using namespace std;

// const array<string, 13> symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

// const array<int, 13> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

unordered_map<string, int> const symbolMap = {
    {"M", 1000}, {"CM", 900}, {"D", 500}, {"CD", 400}, {"C", 100}, {"XC", 90}, {"L", 50}, {"XL", 40}, {"X", 10}, {"IX", 9}, {"V", 5}, {"IV", 4}, {"I", 1}
};

class Solution {
public:
    int romanToInt(string const& s) const {
        int result = 0;
        int i = 0;
        while (i < s.length()) {
            string symbol = s.substr(i, 2);
            if (symbolMap.find(symbol) == symbolMap.end()) {
                symbol = s.substr(i, 1);
                i--;
            }
            result += symbolMap.at(symbol);
            i += 2;
        }
        return result;
    }
};

int main() {
    Solution solution;
    cout << "Solution: " << solution.romanToInt("IVIII") << "\n";
    cout << "Solution: " << solution.romanToInt("I") << "\n";
    cout << "Solution: " << solution.romanToInt("CMDIXI") << "\n";
    return 0;
}
