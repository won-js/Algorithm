package codility;

public class MissingInteger {
	public static void main(String [] args) {
		MissingInteger mi = new MissingInteger();
		int[] A = {1, 3, 6, 4, 1, 2};
		
		System.out.println(mi.solution(A));
	}
	
	public int solution(int[] A) {
		int result = 1;
		int [] nums = new int[1000001];
		
		for(int a : A) {
			if(a >0) {
				nums[a-1] = 1;
			}
		}
		
		for(int i=0; i<nums.length; i++) {
			if(nums[i] == 0) {
				result = i+1;
				break;
			}
		}
		
		return result;
		
    }
}
