vector<int> generate_row(int row){
    int ans = 1;
    vector<int> ans_row;
    ans_row.push_back(1);
    for(int col=1;col<row;col++){
        ans = ans * (row-col);
        ans = ans / (col) ;
        ans_row.push_back(ans);
    }
    return ans_row;
}
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        vector<int> temp;
        for(int i=1;i<numRows+1;i++){
            temp = generate_row(i);
            ans.push_back(temp);
        }
        return ans;
    }
};