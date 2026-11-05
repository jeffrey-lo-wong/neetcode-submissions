class Solution {
public:
    int findMin(vector<int> &nums) {
        // we just need to track where 1 is because we see that if

        // intuitively: we just brute force and create a new array
        // sorting all of them

        // I want to use binary search to find it

        // the middle must be the largest value

        return *min_element(nums.begin(), nums.end());
    
    }
};
