/**
* Class for a bike that has lights
* This will inherit from the bike class
*
* @author Claire Foran 115379021
*/
public abstract class BikeWithLights extends Bike {
    private String frontLight;
    private String rearLight;
    private String bikename;

    /**
    * Constructor for the bike with lights object
    * This also constructs Light objects
    */
    public BikeWithLights(String mybikename){
        super(mybikename);
        Light fLight = new Light();
        Light rLight = new Light();
        fLight.setName("front light");
        rLight.setName("rear light");
        frontLight = fLight.getName();
        rearLight = rLight.getName();
    }

    /**
    * Print the components of the bike with lights
    */
    @Override
    public void printComponents(){
        System.out.println(super.stringBuilder() + " a " + frontLight + ", a " + rearLight);
    }
}

