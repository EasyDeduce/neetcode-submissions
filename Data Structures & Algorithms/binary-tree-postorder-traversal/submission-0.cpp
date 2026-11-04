/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> l;
        if (root==NULL){
            return l;
        }
        if (root->left != NULL){
            vector<int> left =  postorderTraversal(root->left);
            l.insert(l.end(), left.begin(), left.end());
        }
        if (root->right!=NULL){
            vector<int> right = postorderTraversal(root->right);
            l.insert(l.end(), right.begin(), right.end());
        }
        l.push_back(root->val);
        return l;
    }
};