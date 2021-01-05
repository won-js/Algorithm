package leetcode;

import java.util.LinkedList;
import java.util.Queue;

public class MaximumDepthOfBinaryTreeBFS {
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
		if(root == null)
			return 0;
		
		Queue <TreeNode> queue = new LinkedList<>();
		queue.offer(root);
		
		int count = 0;
		while(!queue.isEmpty()) {
			int size = queue.size();
			for(int i=0; i<size; i++) {
				TreeNode node = queue.poll();
				if(node.left != null) {
					queue.offer(node.left);
				}
				if(node.right != null) {
					queue.offer(node.right);
				}
			}
			count++;
		}
		
		return count;
	}
}
