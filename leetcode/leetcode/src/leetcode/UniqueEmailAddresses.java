package leetcode;

import java.util.HashSet;
import java.util.Set;

public class UniqueEmailAddresses {
	public static void main(String [] args ) {
		UniqueEmailAddresses uea = new UniqueEmailAddresses();
		String[] emails = {"test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"};
		
		System.out.println(uea.numUniqueEmails(emails));
	}
	
    public int numUniqueEmails(String[] emails) {
        Set<String> set = new HashSet<>();
        
        for(String email : emails) {
        	int index = email.indexOf('@');
        	String userName = getUser(email,index);
        	String domainName = getDomain(email,index);
        	set.add(userName + '@' + domainName);
        }
        return set.size();
    }
    
    private static String getUser(String email, int index) {
    	StringBuilder sb = new StringBuilder();
    	email = email.substring(0,index);
    	
    	for(char c : email.toCharArray()) {
    		if(c == '+') {
    			break;
    		} else if( c=='.') {
    			continue;
    		} else {
    			sb.append(c);
    		}
    	}
    	return sb.toString();
    }
    
    private static String getDomain(String email,int index) {
    	return email.substring(index+1);
    }
}
