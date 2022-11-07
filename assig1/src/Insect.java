/**
 * Name: Ridwanur Rahman
 * McGill ID: 260828139
 **/

abstract class Insect   {

    private Tile tile;
    private int hp;

    public Insect(Tile tile, int hp)    {
        this.tile = tile;
        this.hp = hp;
        boolean insectAdded = tile.addInsect(this);
        if (!insectAdded) {
            throw new IllegalArgumentException("A bee is already positioned on this tile");
        }
    }

    final Tile getPosition()    {
        return this.tile;
    }

    final int getHealth()   {
        return this.hp;
    }

    public void setPosition(Tile t) {
        this.tile = t;
    }

    public void takeDamage(int damReceived) {
        Tile position = this.getPosition();
        if (this instanceof TankyBee)   {
            //System.out.println(0);
            this.hp -= damReceived;
            if (this.hp <= 0)   {
                position.removeInsect(this.tile.getBee());
            }
        }
        else if (this instanceof HoneyBee && position.isHive() && !(this instanceof TankyBee))   {
            double damage = Math.floor(damReceived*0.9);
            damage = (int) damage;
            this.hp -= damage;
            if (this.hp <= 0)   {
                position.removeInsect(this.tile.getBee());
            }
        }
        else {
            this.hp -= damReceived;
            if (this.hp <= 0)   {
                boolean beeRemoved = position.removeInsect(position.getBee());
                if (!beeRemoved)    {
                    position.removeInsect(position.getHornet());
                }
            }
        }
    }

    public abstract boolean takeAction();

    @Override
    public boolean equals(Object o) {
        if (this == o)  {
            return true;
        }
        if (!(o instanceof Insect)) {
            return false;
        }
        return (this.getPosition() == (((Insect) o).getPosition()) && this.getHealth() == ((Insect) o).getHealth());
    }

}
