package leetcode;

import java.util.Arrays;

public class WidestVertical {
    public int maxWidthOfVerticalArea(int[][] points) {
        Arrays.sort(points,(a,b) -> a[0]-b[0]);
        int before = points[0][0];
        int result = 0;
        
        for(int[] point : points) {
        	if(before == point[0]) {
        		continue;
        	}else {
        		result = Math.max(result, point[0]-before);
        		before = point[0];
        	}
        }
        return result;
    }
}
