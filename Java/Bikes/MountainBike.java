/**
* Class for a mountain bike which inherits the bike class
*
* @author Claire Foran 115379021
*/

public class MountainBike extends Bike {
    private String myFrame;

    /**
    * Constructor for Mountain bike
    */
    public MountainBike() {
        super("mountain bike");
        Frame frame = new Frame();
        frame.setName("low frame");
        myFrame = frame.getName();
    }

    /**
    * Print the components of the bike
    */
    @Override
    public void printComponents(){
        System.out.println(super.stringBuilder() + " and " + myFrame);
    }
}


