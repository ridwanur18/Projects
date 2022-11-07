/**
 * Name: Ridwanur Rahman
 * McGill ID: 260828139
 **/

public class TankyBee extends HoneyBee  {
    private int attdamage;
    private int armor;

    public TankyBee(Tile t, int attdamage, int armor)   {
        super(t, 30, 3);
        this.attdamage = attdamage;
        this.armor = armor;
    }

    public boolean takeAction() {
        Tile t = getPosition();
        if (t.getNumOfHornets() != 0)   {
            Hornet h = t.getHornet();
            h.takeDamage(this.attdamage);
            return true;
        }
        return false;
    }

    @Override
    public void takeDamage(int damReceived) {
        double multiplier = 100.0/(100.0+this.armor);
        damReceived = (int) Math.floor(this.attdamage*multiplier);
        super.takeDamage(damReceived);
    }

    @Override
    public boolean equals(Object o) {
        return super.equals(o) && this.attdamage == ((TankyBee) o).attdamage && this.armor == ((TankyBee) o).armor;
    }
}