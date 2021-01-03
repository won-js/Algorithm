package codility;

public class CyclicRotation {
	public static void main (String [] args) {
		CyclicRotation cr = new CyclicRotation();
		int[] A = {3,8,9,7,6};
		int k = 3;
		
		int[] array = cr.solution(A, k);
		for(int a : array) {
			System.out.println(a);
		}
		
	}
	
	public int[] solution (int[] A, int K) {
		int [] result = new int[A.length];
		for(int i=0; i<A.length; i++) {
			result[(i+K)%A.length] = A[i];
		}
		return result;
	}
}
