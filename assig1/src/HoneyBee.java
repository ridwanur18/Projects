/**
 * Name: Ridwanur Rahman
 * McGill ID: 260828139
 **/

abstract class HoneyBee extends Insect  {
    private int price;

    public HoneyBee(Tile t, int hp, int price)  {
        super(t, hp);
        this.price = price;
    }

    public int getCost()    {
        return this.price;
    }

    @Override
    public boolean equals(Object o) {
        return super.equals(o) && this.getCost() == ((HoneyBee) o).getCost();
    }

}

