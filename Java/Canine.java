public class Canine implements Noise, Roam, Eat {
    
    private final int hungerLevel = 5;
 
    private final Noise concreteNoise;
    private final Roam concreteRoam;
    private final Eat concreteEat;
    private final Boolean eatsGrass = false;

    public Canine() {
        concreteNoise =  new ConcreteNoise("Woof");
        concreteNoise.makeNoise();
        concreteRoam = new ConcreteRoam("Roaming in my pack");
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
        Canine dog = new Canine();
        
    }
}