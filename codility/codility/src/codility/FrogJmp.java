package codility;

public class FrogJmp {
	public static void main(String [] args) {
		FrogJmp fj = new FrogJmp();
		System.out.println(fj.solution(10, 85, 30));
	}
	
	public int solution(int X, int Y, int D) {
		int result = 0;
		if((Y-X)%D == 0) {
			result = (Y-X)/D;
		}else {
			result = (Y-X)/D+1;
		}
		return result;
	}
}
