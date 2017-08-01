/**
* Class for a bike Light
*
* @author Claire Foran 115379021
*/
public class Light {
    private String name;

    /**
    * Constructor for the light
    */
    public Light(){
        name = "light";
    }

    /**
    * Return the name of light as a string
    */
    public String getName(){
        return this.name;
    }

    /**
    * Set the name of the light
    */
    public void setName(String lightName){
        this.name = lightName;
    }
    
}