public class ConcreteRoam implements Roam{
    private final String roam;
 
    public ConcreteRoam(final String roam){
        this.roam = roam;
    }
 
    @Override
    public void roam(){
        System.out.println(roam);
    }
}
