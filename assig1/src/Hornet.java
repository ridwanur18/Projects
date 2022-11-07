/**
 * Name: Ridwanur Rahman
 * McGill ID: 260828139
 **/

public class Hornet extends Insect  {
    private int attdamage;

    public Hornet(Tile t, int hp, int attdamage)   {
        super(t, hp);
        this.attdamage = attdamage;
    }

    public boolean takeAction() {
        Tile tile = this.getPosition();
        if (tile.getBee() != null)    {
            tile.getBee().takeDamage(this.attdamage);
        }
        else if (tile.isHive()) {
            return false;
        }
        else    {
            if (tile.towardTheHive() != null) {
                setPosition(tile.towardTheHive());
                tile.removeInsect(this);
                tile.towardTheHive().addInsect(this);
            }
        }
        return true;

    }

    @Override
    public boolean equals(Object o) {
        return super.equals(o) && this.attdamage == ((Hornet) o).attdamage;
    }

}
