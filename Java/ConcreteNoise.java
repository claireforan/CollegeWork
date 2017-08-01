public class ConcreteNoise implements Noise {
    private final String sound;
 
    public ConcreteNoise(final String sound){
        this.sound = sound;
    }
 
    @Override
    public void makeNoise(){
        System.out.println(sound);
    }   
}