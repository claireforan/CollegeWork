public class Hippo implements Noise, Roam, Eat {
    
    private final int hungerLevel = 5;
 
    private final Noise concreteNoise;
    private final Roam concreteRoam;
    private final Eat concreteEat;
    private final Boolean eatsGrass = true;
 
    public Hippo() {
        concreteNoise =  new ConcreteNoise("Grr");
        concreteNoise.makeNoise();
        concreteRoam = new ConcreteRoam("I'm lazy, I dont not roam");
        concreteRoam.roam();
        concreteEat = new ConcreteEat("I eat "+ hungerLevel + " portions of ");
        concreteEat.eat();
    }

    
    @Override
    public void roam() { 
        concreteNoise.makeNoise( );
    }

    @Override
    public void makeNoise() { 
        concreteNoise.makeNoise( );
    }
    
    @Override
    public void eat() { 
        concreteEat.eat(); 
    }

    public static void main(String[] args){
        Hippo hippy = new Hippo();
        
    }
}