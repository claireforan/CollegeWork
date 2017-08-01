public class List{
    private Link link;

    public List() {
        link = null;
    }

    public void add ( int value ) {
        link = new Link( link, value);
    }

    public void print() {
        Link.print(link);
    }

    // Does not need access to attributes of the outer class so it is static
    // This also makes it faster
    private static class Link {
        private int value;
        private Link next;


        private Link( final Link link, final int value ){
            this.value = value;
            this.next = link;
        }
        private static Link add( final Link link, final int value){
            return link;
        }

        private static void print(final Link link){
            if (link != null){
                System.out.println(link.value);
                print(link.next);
            }
        }
    }
}