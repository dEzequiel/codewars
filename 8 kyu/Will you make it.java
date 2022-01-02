public class Kata {

  public static boolean zeroFuel(double distanceToPump, double mpg, double fuelLeft) {
    // Your code here!
    double suficiente = mpg * fuelLeft;
    if(distanceToPump <= suficiente) {
      return true;
    } else {
      return false;
    }
  }

}