/*
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.
*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string> const & strs) const {
        size_t prefixLength = strs[0].length();
        for (size_t i = 1; i < strs.size(); i++) {
            if (prefixLength == 0) {
                break;
            }
            int j = 0;
            while (j < prefixLength && j < strs[i].length() && 
            strs[0][j] == strs[i][j]) {
                j++;
            }
            prefixLength = j;
        }
        return strs[0].substr(0, prefixLength);
    }
};

int main() {
    Solution solution;
    cout << solution.longestCommonPrefix({"flower", "flow", "flight"}) << "\n";
    cout << solution.longestCommonPrefix({"dog", "racecar", "car"}) << "\n";
    return 0;
}