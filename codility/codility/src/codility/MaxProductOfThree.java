package codility;

import java.util.Arrays;

public class MaxProductOfThree {
	public static void main(String [] args) {
		MaxProductOfThree mp = new MaxProductOfThree();
		int[] A = {-3,1,2,-2,5,6};
		System.out.println(mp.solution(A));
	}
	
    public int solution(int[] A) {
    	Arrays.sort(A);

    	int left = A[0]*A[1]*A[A.length-1];
    	int right = A[A.length-3]*A[A.length-2]*A[A.length-1];
    	
    	return Math.max(left, right);
    }
}
