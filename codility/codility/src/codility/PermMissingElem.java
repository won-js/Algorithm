package codility;

public class PermMissingElem {
	public static void main(String [] args) {
		PermMissingElem pme = new PermMissingElem();
		int[] A = {2,3,1,5};
		
		System.out.println(pme.solution(A));
	}
	
	public int solution(int[] A) {
		int[] nums = new int[A.length+1];
		int result = 0;
		for (int a : A) {
			nums[a-1]++;
		}
		
		for(int i =0; i<nums.length; i++) {
			if(nums[i] == 0) {
				result =i+1;
				break;
			}
		}
		return result;
    }
}
