class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        for(int i =1; i< brown+1; i++){
            if((brown/2 - i+2) * i == brown+yellow ){
                answer[0] = i;
                answer[1] = brown/2 - i + 2;
            }
        }
        
        return answer;
    }
}

// yellow, brown
// 정사각형 vs 직사각형
// 정사각형 => n^2 (1,4,9,16...)
// 직사각형 => 정사각형이 아니면 무조건 직사각형.
// brown 을 잘 쪼개서, a*b = brown + yellow 확인 
