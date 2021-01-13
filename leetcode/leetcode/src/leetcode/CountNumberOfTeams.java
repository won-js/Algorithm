package leetcode;

import java.util.HashSet;
import java.util.Set;

public class CountNumberOfTeams {
    public int numTeams(int[] rating) {
        Set<int []> set = new HashSet<>();
        int len = rating.length;
        
        for(int i=0; i<len-2; i++) {
        	for(int j=i+1; j<len-1; j++) {
        		for(int k=j+1; k<len; k++) {
        			if(rating[i] < rating[j]) {
        				if(rating[j]<rating[k]) {
        					int[] temp = {rating[i],rating[j],rating[k]};
        					set.add(temp);
        				}
        			}else {
        				if(rating[j]>rating[k]) {
        					int[] temp = {rating[i],rating[j],rating[k]};
        					set.add(temp);
        				}
        			}
        		}
        	}
        }
        
        return set.size();
    }
}
