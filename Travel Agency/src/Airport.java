//Name: Ridwanur Rahman
//ID: 260828139

public class Airport {
	
	private int xcoord;
	private int ycoord;
	private int fees;
	
	public Airport(int xcoord, int ycoord, int fees) {
		
		this.xcoord = xcoord;
		this.ycoord = ycoord;
		this.fees = fees;
		
	}
	
	public int getFees() {
		
		return this.fees;
		
	}
	
	public static int getDistance(Airport a1, Airport a2) {
		
		double xdiff = a1.xcoord - a2.xcoord;
		double ydiff = a1.ycoord - a2.ycoord;
		
		double distance = Math.sqrt(Math.pow(xdiff, 2) + Math.pow(ydiff, 2));
		
		distance = Math.ceil(distance);
		
		return (int) distance;
		
	}
	
}
