package leetcode;

public class Solution {
	public static void main(String [] args) {
		Solution s = new Solution();
		int[] arr1 = {9, 20, 28, 18, 11};
		int[] arr2 = {30, 1, 21, 17, 28};
		
		s.solution(5, arr1, arr2);
	}
	
	public String[] solution(int n, int[] arr1, int[] arr2) {
		String[] answer = new String[arr1.length];
		int len = arr1.length;
		for(int i=0; i<arr1.length; i++) {
			answer[i] = sum(toTwo(arr1[i],len),toTwo(arr2[i],len));
		}
        return answer;
    }
	
	//2진법으로 만드는 메소드
	private String toTwo(int num, int length) {
		String answer = "";
		while(num != 0) {
			answer += num%2;
			num /= 2;
		}
		if(answer.length() < length) {
			for(int i=0; i<length-answer.length(); i++) {
				answer = '0'+answer;
			}
		}
		return answer;
	}
	
	//string 두개 합쳐서 해독
	private String sum(String a, String b) {
		String answer = "";
		System.out.println(a);
		for(int i=0; i<a.length(); i++) {
			if(Integer.valueOf(a.charAt(i))+Integer.valueOf(b.charAt(i))==0) {
				answer += ' ';
			}else {
				answer += '#';
			}
		}
		return answer;
	}
}
