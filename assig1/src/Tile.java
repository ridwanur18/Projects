/**
 * Name: Ridwanur Rahman
 * McGill ID: 260828139
 **/

public class Tile {
    private int food;
    private boolean beehive;
    private boolean hornetNest;
    private boolean nestToHivePath;
    private Tile nestToHive;
    private Tile hiveToNest;
    private HoneyBee honBee;
    private SwarmOfHornets hornetsSwarm;

    public Tile()   {
        this.beehive = false;
        this.hornetNest = false;
        this.nestToHivePath = false;
        this.food = 0;
        this.honBee = null;
        this.hornetsSwarm = new SwarmOfHornets();
    }

    public Tile(int food, boolean beehive, boolean hornetNest, boolean nestToHivePath, Tile nestToHive, Tile hiveToNest, HoneyBee honBee, SwarmOfHornets hornetsSwarm) {
        this.food = food;
        this.beehive = beehive;
        this.hornetNest = hornetNest;
        this.nestToHivePath = nestToHivePath;
        this.nestToHive = nestToHive;
        this.hiveToNest = hiveToNest;
        this.honBee = honBee;
        this.hornetsSwarm = hornetsSwarm;
    }

    public boolean isHive() {
        return this.beehive;
    }

    public boolean isNest() {
        return this.hornetNest;
    }

    public void buildHive() {
        this.beehive = true;
    }

    public void buildNest() {
        this.hornetNest = true;
    }

    public boolean isOnThePath()    {
        return this.nestToHivePath;
    }

    public Tile towardTheHive() {
        if (this.isOnThePath()) {
            return nestToHive;
        }
        return null;
    }

    public Tile towardTheNest() {
        if (this.isOnThePath())    {
            return hiveToNest;
        }
        return null;
    }

    public void createPath(Tile towardHive, Tile towardNest)    {
        this.nestToHive = towardHive;
        this.hiveToNest = towardNest;
        this.nestToHivePath = true;
    }

    public int collectFood()    {
        int foodCollected = this.food;
        this.food = 0;
        return foodCollected;
    }

    public void storeFood(int f) {
        this.food += f;
    }

    public HoneyBee getBee()    {
        return this.honBee;
    }

    public Hornet getHornet()   {
        return this.hornetsSwarm.getFirstHornet();
    }

    public int getNumOfHornets()    {
        return this.hornetsSwarm.sizeOfSwarm();
    }

    public boolean addInsect(Insect insect) {
        int x = 0;
        if (insect instanceof HoneyBee) {
            if ((getBee() == null) && (!isNest())) {
                insect.setPosition(this);
                this.honBee = (HoneyBee) insect;
                return true;
            }
        } else  {
            if (isNest() || isHive() || isOnThePath()) {
                insect.setPosition(this);
                this.hornetsSwarm.addHornet((Hornet) insect);
                return true;
            }
        }
        return false;
    }

    public boolean removeInsect(Insect insect)  {
        Tile currentTile = insect.getPosition();
        if (currentTile != null)    {
            if (insect instanceof Hornet)   {
                this.hornetsSwarm.removeHornet((Hornet) insect);
                if (this.getNumOfHornets() == 0)    {
                    insect.setPosition(null);
                }
            }
            else {
                insect.setPosition(null);
                this.honBee = null;
            }
            return true;
        }
        return false;
    }
}

