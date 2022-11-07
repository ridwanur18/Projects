/**
 * Name: Ridwanur Rahman
 * McGill ID: 260828139
 **/

public class BusyBee extends HoneyBee   {

    public BusyBee(Tile t)  {
        super(t, 5, 2);
    }

    @Override
    public boolean takeAction() {
        Tile t = getPosition();
        t.storeFood(2);
        return true;
    }

}