package leetcode;

import java.util.ArrayList;
import java.util.List;

public class GenerateParentheses {
    public List<String> generateParenthesis(int n) {
    	List<String> result = new ArrayList<>();
    	dfs(result,"", n , n);
    	return result;
    }
    
    private void dfs(List<String> result, String str, int left, int right) {
    	//1 제약조건
    	if(left < 0 || left > right) return;
    	
    	//2
    	if(left == 0 && right == 0) {
    		result.add(str);
    		return;
    	}
    	dfs(result, str+"(", left-1, right);
    	dfs(result, str+")", left, right-1);
    }
}
