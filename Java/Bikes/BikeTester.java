/**
* Class for Bike testing
*
* @author Claire Foran 115379021
*/
public class BikeTester {

    public static void main(String[] args){

        
        Bike mymountainbike = new MountainBike();
        mymountainbike.printComponents();

        Bike mycitybike = new CityBike();
        mycitybike.printComponents();

        Bike myhybridbike = new Hybrid();
        myhybridbike.printComponents();
    
    }

}
