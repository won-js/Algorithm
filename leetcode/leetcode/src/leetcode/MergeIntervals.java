package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeIntervals {
	public int[][] merge(int[][] intervals) {
		List<int[]> result = new ArrayList<>();
		
		Arrays.sort(intervals, (a,b) -> a[0]- b[0]);
		
		int[] before = intervals[0];
		for(int i=1; i<intervals.length; i++)  {
			if(before[1] >= intervals[i][0]) {
				before[1] = Math.max(before[1], intervals[i][1]);
			} else {
				result.add(before);
				before = intervals[i];
			}
		}
		
		if(!result.contains(before)) {
			result.add(before);
		}
		
		return result.toArray(new int[result.size()][2]);
	}
}
