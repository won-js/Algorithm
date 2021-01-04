package leetcode;

public class LicenseKeyFormatting {
	public static void main(String [] args) {
		LicenseKeyFormatting lk = new LicenseKeyFormatting();
		String S = "5F3Z-2e-9-w";
		
		System.out.println(lk.licenseKeyFormatting(S,4));
	}
	
    public String licenseKeyFormatting(String S, int K) {
    	StringBuilder sb = new StringBuilder();
    	
    	for(char c : S.toUpperCase().toCharArray()) {
    		if(c != '-') sb.append(c);
    	}
    	
    	for(int i=sb.length()-K; i>0; i -= K) {
    		sb.insert(i, '-');
    	}
    	
    	return sb.toString();
    }
}
