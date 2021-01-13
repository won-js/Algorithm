package leetcode;

public class MaximumBinaryString {
    public static void main(String [] args) {
    	MaximumBinaryString m = new MaximumBinaryString();
    	System.out.println(m.maximumBinaryString("binary = '000110'"));
    }
	
	
	public String maximumBinaryString(String binary) {
        String num = binary.substring(10,binary.length()-1);
        
        return num;
    }
}
