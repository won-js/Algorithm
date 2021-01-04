package codility;

public class CountDiv {
	public static void main(String[] args) {
		CountDiv cd = new CountDiv();
		System.out.println(cd.solution(6, 11, 2));
	}

	public int solution(int A, int B, int K) {
		return B / K - A / K + (A % K == 0 ? 1 : 0);
	}
}
