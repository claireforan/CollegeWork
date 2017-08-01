/**
* Class for a city bike which inherits the bike with lights class
*
* @author Claire Foran 115379021
*/

public class CityBike extends BikeWithLights {
    private String myCarrier;
    private String myFrame;

    /**
    * Constructor for City bike
    */
    public CityBike(){
        super("city bike");
        Frame frame = new Frame();
        frame.setName("high frame");
        myFrame = frame.getName();
        Carrier carrier = new Carrier();
        myCarrier = carrier.getName();
    }

    /**
    * Print the components of the bike
    */
    @Override
    public void printComponents(){
        System.out.println(super.stringBuilder() + ", a " + myCarrier + " and a " + myFrame);
    }


}
