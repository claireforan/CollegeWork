/**
* Class for a general bike with brakes, 
* saddle, handlebar and wheels
*
* @author Claire Foran 115379021
*/
public abstract class Bike {
    private String myBrakes;
    private String myWheels;
    private String mySaddle;
    private String myHandlebar;
    
    private String bikename;

    /**
    * Constructor for bike
    */
    public Bike(String mybikename){
        
        bikename = mybikename;

        Brakes brakes = new Brakes();
        brakes.setName(" brakes");
        myBrakes = brakes.getName();

        Wheels wheels = new Wheels();
        wheels.setName("2 wheels");
        myWheels = wheels.getName();

        Saddle saddle = new Saddle();
        saddle.setName("saddle");
        mySaddle = saddle.getName();

        Handlebar handlebar = new Handlebar();
        handlebar.setName("handlebar");
        myHandlebar = handlebar.getName();

    }

    /**
    * Builds and returns a string containing all components of the bike
    */
    public String stringBuilder(){
        return "This " + bikename + " has " + myBrakes + ", " + myWheels + ", a " + mySaddle + ", a " + myHandlebar;
    }

    /**
    * Print the components of the bike
    */
    public abstract void printComponents();
}

