public class ConcreteEat implements Eat {
    private final String eat;
 
    public ConcreteEat(final String eat){
        this.eat = eat;
    }
 
    @Override
    public void eat(){
        System.out.println(eat);
    }   
}

