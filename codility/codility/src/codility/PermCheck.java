package codility;

public class PermCheck {
	public static void main(String [] args) {
		PermCheck pc = new PermCheck();
		int[] A1 = {4,1,3,2};
		int[] A2 = {4,1,3};
		
		System.out.println(pc.solution(A1));
		System.out.println(pc.solution(A2));
	}
	
	public int solution(int[] A) {
		int[] nums = new int[1000000];
		int result = 1;
		
		for(int a : A) {
			if(a > 1000000) return 0;
			if(nums[a-1] == 0) {
				nums[a-1] = 1;
			} else {
				result = 0;
				return result;
			}
		}
		
		for(int i=0; i<A.length; i++) {
			if(nums[i] == 0) {
				result =0;
				break;
			}
		}
		
		return result;
	}
}
