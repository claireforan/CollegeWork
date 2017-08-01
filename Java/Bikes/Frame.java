/**
* Class for frame object
*
* @author Claire Foran 115379021
*/
public class Frame {
    private String name;

    /**
    * Constructor for the frame
    */
    public Frame(){
        name = "frame";
    }

    /**
    * Return the name of the frame
    */
    public String getName(){
        return this.name;
    }

    /**
    * Set the name of the frame
    */
    public void setName(String frameName){
        this.name = frameName;
    }

}