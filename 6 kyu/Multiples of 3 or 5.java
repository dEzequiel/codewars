public class Solution {

  public int solution(int number) {
    //TODO: Code stuff here
    int sum = 0;
    for(int i = 0; i < number; i++) {
      if(i%3==0){
        sum += i;
      }
      else if(i%5==0){
        sum += i;
      }
      else if(number < 0) {
        return 0;
      }
    }
    return sum;
  }
}