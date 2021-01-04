package leetcode;

public class PlusOne {
	public static void main(String [] args ) {
		PlusOne po = new PlusOne();
		
	}
	
	public int[] plusOne(int[] digits) {
		int index = digits.length -1;
		int carry = 1;
		
		while(index >= 0 && carry>0) {
			digits[index] = (digits[index]) % 10;
			if(digits[index] == 0) {
				carry = 1;
			}else {
				carry = 0;
			}
			index--;
		}
		
		if(carry == 1) {
			digits = new int[digits.length+1];
			digits[0] =1;
		}
		
		return digits;
	}
}
