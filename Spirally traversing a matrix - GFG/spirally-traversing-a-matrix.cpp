//{ Driver Code Starts
#include <bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
class Solution
{   
    public: 
    //Function to return a list of integers denoting spiral traversal of matrix.
    vector<int> spirallyTraverse(vector<vector<int> > matrix, int r, int c) 
    {
        int n = matrix.size();
        int m = matrix[0].size();
        int l = 0, t = 0, b = n - 1, rr = m - 1;
        vector<int> ans;

        while (l <= rr && t <= b) {
            for (int i = l; i <= rr; i++) {
                ans.push_back(matrix[t][i]);
            }
            t++;

            for (int i = t; i <= b; i++) {
                ans.push_back(matrix[i][rr]);
            }
            rr--;

            if (t <= b) {
                for (int i = rr; i >= l; i--) {
                    ans.push_back(matrix[b][i]);
                }
                b--;
            }

            if (l <= rr) {
                for (int i = b; i >= t; i--) {
                    ans.push_back(matrix[i][l]);
                }
                l++;
            }
        }

        return ans;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin>>t;
    
    while(t--) 
    {
        int r,c;
        cin>>r>>c;
        vector<vector<int> > matrix(r); 

        for(int i=0; i<r; i++)
        {
            matrix[i].assign(c, 0);
            for( int j=0; j<c; j++)
            {
                cin>>matrix[i][j];
            }
        }

        Solution ob;
        vector<int> result = ob.spirallyTraverse(matrix, r, c);
        for (int i = 0; i < result.size(); ++i)
                cout<<result[i]<<" ";
        cout<<endl;
    }
    return 0;
}
// } Driver Code Ends