package leetcode;

import java.util.Stack;

public class MaximumDepthOfBinaryTreeDFS {
	public static void main(String [] args) {
		TreeNode tree = new TreeNode(3);
		tree.left = new TreeNode(1);
		tree.right = new TreeNode(4);
		tree.left.left = new TreeNode(5);
		tree.left.right = new TreeNode(8);
		tree.left.left.left = new TreeNode(7);
		
		MaximumDepthOfBinaryTree md = new MaximumDepthOfBinaryTree();
		System.out.println(md.maxDepth(tree));
	}
	
	public int maxDepth(TreeNode root) {
		//1
		if(root == null ) 
			return 0;
		
		Stack<TreeNode> stack = new Stack<>();
		Stack<Integer> valueStack = new Stack<>();
		stack.push(root);
		valueStack.push(1); // 현재 레벨
		int max = 0;
		
		while(!stack.isEmpty()) {
			TreeNode node = stack.pop();
			int count = valueStack.pop();
			max = Math.max(max, count);
			
			if(node.left != null) {
				stack.push(node.left);
				valueStack.push(1+count);
			}
			if(node.right != null) {
				stack.push(node.right);
				valueStack.push(1+count);
			}
		}
		return max;
	}
}
