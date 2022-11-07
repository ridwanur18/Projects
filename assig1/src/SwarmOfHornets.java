/**
 * Name: Ridwanur Rahman
 * McGill ID: 260828139
 **/

public class SwarmOfHornets {
    private Hornet[] hornets;
    private int size;

    public SwarmOfHornets() {
        this.hornets = new Hornet[this.sizeOfSwarm()];
    }

    public int sizeOfSwarm() {
        return this.size;
    }

    public Hornet[] getHornets() {
        return this.hornets;
    }

    public Hornet getFirstHornet() {
        Hornet[] curHornets = this.getHornets();
        if (curHornets.length == 0) {
            return null;
        } else {
            return curHornets[0];
        }
    }

    private void helper(Hornet h, Hornet[] hornets) {
        this.size++;
        int newLength = this.sizeOfSwarm();
        Hornet[] temp = hornets;
        hornets = new Hornet[newLength];
        for (int i=0; i<temp.length; i++)   {
            hornets[i] = temp[i];
        }
        hornets[newLength - 1] = h;
        this.hornets = hornets;
    }

    public void addHornet(Hornet h) {
        Hornet[] hornets = this.hornets;
        if (hornets.length > 0) {
            if (hornets[this.sizeOfSwarm() - 1] != null) {
                helper(h, hornets);
            }
            else {
                hornets[this.sizeOfSwarm() - 1] = h;
            }
        }
        else    {
            this.size++;
            hornets = new Hornet[this.sizeOfSwarm()];
            hornets[0] = h;
            this.hornets = hornets;
        }
    }

    public boolean removeHornet(Hornet h)   {
        Hornet[] hornets = this.getHornets();
        for (int i=0; i<hornets.length; i++)   {
            if (hornets[i] == h)   {
                Hornet[] newHornets = new Hornet[hornets.length-1];
                if (i == hornets.length-1)  {
                    for (int j=0; j<newHornets.length; j++) {
                        newHornets[j] = hornets[j];
                    }
                }
                else {
                    for (int j=0; j<i; j++)    {
                        newHornets[j] = hornets[j];
                    }
                    for (int j=i; j<newHornets.length; j++)    {
                        newHornets[j] = hornets[j+1];
                    }
                }
                this.size--;
                this.hornets = newHornets;
                return true;
            }
        }
        return false;
    }
}