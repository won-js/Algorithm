package leetcode;

public class RomanToIneteger {
	public static void main(String [] args) {
		RomanToIneteger rti = new RomanToIneteger();
		String s = "III";
		
		System.out.println(rti.romanToInt(s));
		
	}
	
    public int romanToInt(String s) {
        int result = 0;
        char[] array = s.toCharArray();
        char before = 'a';
        
    	for(int i = 0; i<array.length-1; i++) {
    		switch(array[i]) {
    			case 'I':
    				if(array[i+1] == 'V' || array[i+1] == 'X') {
    					before = 'I';
    				}else {
    					result += 1;
    				}
    				break;
    			case 'V':
    				if(before == 'I') {
    					result += 4;
    					before = 'a';
    				}else {
    					result += 5;
    				}
    				break;
    			case 'X':
    				if(before == 'I') {
    					result += 9;
    					before = 'a';
    				}else {
    					if(array[i+1] == 'C' || array[i+1] == 'L') {
    						before = 'X';
    					}else {
    						result += 10;
    					}
    				}
    				break;
    			case 'L':
    				if(before == 'X') {
    					result += 40;
    					before = 'a';
    				} else {
    					result += 50;
    				}
    				break;
    			case 'C':
    				if(before == 'X') {
    					result += 90;
    					before = 'a';
    				}else {
    					if(array[i+1] == 'M') {
    						before = 'C';
    					}else {
    						result += 100;
    					}
    				}
    				break;
    			case 'D':
    				if(before == 'M') {
    					result += 400;
    					before = 'a';
    				} else {
    					result += 500;
    				}
    				break;
    			case 'M':
    				if(before == 'M') {
    					result += 900;
    					before = 'a';
    				} else {
    					result += 1000;
    				}
    				break;
    		}
    	}
    	return result;
    }
}
