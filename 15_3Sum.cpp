/*
LeetCode 15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
*/

#include <iostream>
#include <vector>
#include <string> 

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
        auto iterStart = nums.begin() + negativeEnd;
        auto iterEnd = nums.begin() + nums.size();
        inner(nums, negativeStart, negativeEnd, iterStart, iterEnd, result);
        iterStart = nums.begin() + negativeStart;
        iterEnd = nums.begin() + negativeEnd;
        inner(nums, negativeEnd, nums.size(), iterStart, iterEnd, result);
        return result;
    }
    void test(vector<int>& nums) {
        cout << "Input: [";
        for (size_t i = 0; i < nums.size(); i++) {
            cout << nums[i] << (i < nums.size() - 1 ? ", " : "");
        }
        cout << "], Result: ";
        auto answer = threeSum(nums);
        for (size_t i = 0; i < answer.size(); i++) {
            cout << "[" << answer[i][0] << ", ";
            cout << answer[i][1] << ", ";
            cout << answer[i][0] << "]" << (i < answer.size() - 1 ? ", " : "");
        }
        cout << "\n\n";
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
    nums = { 1, -1, 0 };
    solution.test(nums);
    nums = { 10, -10, 5, 5 };
    solution.test(nums);
    nums = { 0, 0, 0, 0 };
    solution.test(nums);
    return 0;
}