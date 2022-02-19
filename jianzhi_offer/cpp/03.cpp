class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
       set<int> seen;
       for (const auto& i: nums) {
           if (seen.find(i) != seen.end()) {
               return i;
           } else {
               seen.emplace(i);
           }
       }
       return -1;
    }
};