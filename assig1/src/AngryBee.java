/**
 * Name: Ridwanur Rahman
 * McGill ID: 260828139
 **/

public class AngryBee extends HoneyBee  {
    private int attdamage;

    public AngryBee(Tile t, int attdamage)  {
        super(t, 10, 1);
        this.attdamage = attdamage;
    }

    public boolean takeAction() {
        Tile t = getPosition();
        Tile search = getPosition();
        if (t.isHive() || t.isOnThePath())  {
            while (!((search.getHornet() != null) && (!search.isNest()) && (search != null))) {
                search = search.towardTheHive();
            }
            Hornet h = search.getHornet();
            h.takeDamage(this.attdamage);
            return true;
        }
        return false;
    }

    @Override
    public boolean equals(Object o) {
        return super.equals(o) && this.attdamage == ((AngryBee) o).attdamage;
    }

}