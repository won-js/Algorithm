package leetcode;

public class MoveZeroes {
	public static void main (String [] args ) {
		MoveZeroes mz = new MoveZeroes();
		int[] A = {0,1,0,3,12};
		mz.moveZeroes(A);
		for(int a : A) {
			System.out.println(a);
		}
	}
	
	
	public void moveZeroes(int[] nums) {
		int index = 0;
		
		for(int num : nums) {
			if(num !=0) {
				nums[index++] = num;
			}
		}
		
		while(index < nums.length) {
			nums[index++] = 0;
		}
		
	}
}
