/**
* Class for a hibrid bike which inherits the bike with lights class
*
* @author Claire Foran 115379021
*/

public class Hybrid extends Bike {
    private String myFrame;
    private String frontLights;
    private String rearLights;

    /**
    * Constructor for Hybrid bike
    */
    public Hybrid(){
        super("hybrid bike");
        Frame frame = new Frame();
        frame.setName("medium frame");
        myFrame = frame.getName();
    }

    /**
    * Print the components of the bike
    */
    @Override
    public void printComponents(){
        System.out.println( super.stringBuilder() + " and a " + myFrame );
    }

}