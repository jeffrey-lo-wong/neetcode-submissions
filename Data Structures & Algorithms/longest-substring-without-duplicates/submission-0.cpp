class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int last[256];
        fill(begin(last), end(last), -1);

        int best = 0, left = 0;
        for (int r = 0; r < (int)s.size(); ++r) {
            unsigned char c = s[r];
            if (last[c] >= left) {
                left = last[c] + 1;
            }
            last[c] = r;
            best = max(best, r - left + 1);
        }
        return best;
    }
};
