package leetcode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode() {
	}

	TreeNode(int val) {
		this.val = val;
	}

	TreeNode(int val, TreeNode left, TreeNode right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}
}

public class BinaryTreeLevelOrderTraversal {
	public static void main(String[] args) {
		BinaryTreeLevelOrderTraversal bt = new BinaryTreeLevelOrderTraversal();
		TreeNode root = new TreeNode(3);
		root.left = new TreeNode(9);
		root.right = new TreeNode(20);
		root.right.left = new TreeNode(15);
		root.right.right = new TreeNode(7);
	
		System.out.println(bt.levelOrder(root));
	}

	public List<List<Integer>> levelOrder(TreeNode root) {
		List<List<Integer>> array = new ArrayList<>();
		List<List<Integer>> result = new ArrayList<>();
		
		if(root == null)
			return result;
		Queue<TreeNode> queue = new LinkedList<>();
		queue.offer(root);
		
		//2
		while(!queue.isEmpty()) {
			int size = queue.size();
			List<Integer> list = new LinkedList<>();
			for(int i=0; i<size; i++) {
				TreeNode node = queue.poll();
				list.add(node.val);
				if(node.left != null) {
					queue.offer(node.left);
				}
				if(node.right != null) {
					queue.offer(node.right);
				}
			}
			array.add(list);
		}
		for(int i= array.size()-1 ; i>=0; i--) {
			result.add(array.get(i));
		}
		
		return result;
	}
}
