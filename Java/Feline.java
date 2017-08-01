public class Feline implements Noise, Roam, Eat {
    private final int hungerLevel = 2;
 
    private final Noise concreteNoise;
    private final Roam concreteRoam;
    private final Eat concreteEat;
    private final Boolean eatsGrass = false;
 
    public Feline() {
        concreteNoise =  new ConcreteNoise("Meow");
        concreteNoise.makeNoise();
        concreteRoam = new ConcreteRoam("Roaming alone");
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
        Feline cat = new Feline();
        
    }
}