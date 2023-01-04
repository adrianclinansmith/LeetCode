/*
LeetCode 15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result = {};
        sort(nums.begin(), nums.end());
        size_t negativeStart = 0, negativeEnd = 0;
        while (negativeEnd < nums.size() && nums[negativeEnd] < 0) {
            negativeEnd++;
        }
        size_t positiveStart = negativeEnd, positiveEnd = nums.size();
        auto iterStart = nums.begin() + positiveStart;
        auto iterEnd = nums.begin() + positiveEnd;
        inner(nums, negativeStart, negativeEnd, iterStart, iterEnd, result);
        iterStart = nums.begin() + negativeStart;
        iterEnd = nums.begin() + negativeEnd;
        inner(nums, positiveStart, positiveEnd, iterStart, iterEnd, result);
        return result;
    }
    void test(vector<int>& nums) {
        cout << "*~*~*~*~*~*~*~*\nInput:\n*~*~*~*~*~*~*~*\n";
        for (int num : nums) {
            cout << num << ", ";
        }
        cout << "\n\nSorted:\n";
        sort(nums.begin(), nums.end());
        for (int num : nums) {
            cout << num << ", ";
        }
        cout << "\n\nResult:\n";
        vector<vector<int>> result = threeSum(nums);
        for (vector<int>& tri : result) {
            cout << tri[0] << ", " << tri[1] << ", " << tri[2] << "\n";
        }
        cout << "\n";
    } 
private:
    void inner(vector<int>& nums, size_t loopStart, size_t loopEnd, vector<int>::iterator iterStart, vector<int>::iterator iterEnd, vector<vector<int>>& result) {
        for (size_t i = loopStart; i < loopEnd; i++) {
            if (i > loopStart && nums[i] == nums[i-1]) {
                continue;
            }
            for (size_t k = i + 1; k < loopEnd; k++) {
                if (k > i + 1 && nums[k] == nums[k-1]) {
                    continue;
                }
                int toFind = -(nums[i] + nums[k]);
                if (binary_search(iterStart, iterEnd, toFind)) {
                    result.push_back({nums[i], nums[k], toFind});
                }
            }    
        }
    }
};

int main() {
    Solution solution;
    vector nums = { 1, 2, -3, 4 };
    solution.test(nums);
    nums = { -1, 2, -1, -3, 4 };
    solution.test(nums);
    nums = { 1, 1, 1, 1 };
    solution.test(nums);
    return 0;
}