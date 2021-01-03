package codility;

public class TapeEquilibrium {
	public static void main(String[] args) {
		TapeEquilibrium te = new TapeEquilibrium();
		int[] A = { 3, 1, 2, 4, 3 };

		System.out.println(te.solution(A));
	}

	public int solution(int[] A) {
		int left = A[0];
		int total = 0;
		
		for(int a : A) {
			total += a;
		}
		
		int min = Math.abs(2*left - total);
		int current;
		
		for(int i=1; i<A.length - 1 ; i++) {
			left += A[i];
			current = Math.abs(2*left - total);
			if(min > current) min = current;
		}
		
		return min;
		
	}
}
