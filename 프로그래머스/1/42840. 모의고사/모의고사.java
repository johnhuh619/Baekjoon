import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] p1 = {1, 2, 3, 4, 5};
        int[] p2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] p3 = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] score = {0, 0, 0};
        
        for(int i=0;i<answers.length; i++){
            if(answers[i] == p1[i%5]) score[0] += 1;
            if(answers[i] == p2[i%8]) score[1] += 1;
            if(answers[i] == p3[i%10]) score[2] += 1;
        }
        int max = Math.max(score[0], Math.max(score[1],score[2]));
        
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i =0; i<score.length; i++){
            if(score[i] == max){
                arr.add(i+1);
            }
        }
        return arr.stream().mapToInt(i->i).toArray();
    }
}