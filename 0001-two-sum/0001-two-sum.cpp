class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> mp;
        for(int i=0;i<nums.size();i++){
            int a = nums[i];
            int rem = target - a;
            if(mp.find(rem) != mp.end()){
                return{mp[rem],i};
            }
            mp[a] = i;
        }
        return {-1,-1};
    }
};