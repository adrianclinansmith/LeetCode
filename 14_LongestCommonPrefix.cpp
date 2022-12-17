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
    string longestCommonPrefix(vector<string> const& strs) const {
        string prefix = strs[0];
        for (auto iter = strs.cbegin() + 1; iter != strs.cend(); ++iter) {
            int i = 0;
            while (i < prefix.length() && i < (*iter).length() && prefix[i] == (*iter)[i]) {
                i++;
            }
            prefix = prefix.substr(0, i);
        }
        return prefix;
    }
};

int main() {
    Solution solution;
    cout << solution.longestCommonPrefix({"flower", "flow", "flight"}) << "\n";
    cout << solution.longestCommonPrefix({"dog", "racecar", "car"}) << "\n";
    return 0;
}