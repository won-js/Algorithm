package leetcode;

public class PalindromeNumber {
	public static void main(String [] args) {
		PalindromeNumber pn = new PalindromeNumber();
		int x = -121;
		
		System.out.println(pn.isPalindrome(x));
	}
	
//    public boolean isPalindrome(int x) {
//    	char[] array = String.valueOf(x).toCharArray();
//    	if(array.length % 2!=0) {
//    		int index =0;
//    		int mid = array.length/2;
//    		while(mid-index >= 0) {
//    			if(array[mid-index] != array[mid+index]) return false;
//    			index++;
//    		}
//    	}else {
//    		int right = array.length/2;
//    		int left = right-1;
//    		while(left>=0) {
//    			if(array[left] != array[right]) return false;
//    			left--;
//    			right++;
//    		}
//    		
//    	}
//    	return true;
//    }
	
	public boolean isPalindrome(int x) {
		if(x < 0 || (x%10 == 0 && x != 0)) {
			return false;
		}
		
		int num = x;
		int y = 0;
		while(num != 0) {
			int temp = num%10;
			num /= 10;
			y = y*10 + temp;
		}
		
		return x == y;
	}
}
