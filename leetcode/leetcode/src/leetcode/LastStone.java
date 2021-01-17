package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LastStone {
    public int lastStoneWeight(int[] stones) {
        Arrays.sort(stones);
        List<Integer> list = new ArrayList<>();
        list.sort((a,b) -> a-b);
        while(stones.length > 1) {
        	if(stones[stones.length-1] == stones[stones.length-2]) {
        		int[] array = new int[stones.length-2];
        		
        	}else {
        		
        	}
        }
    }
}
