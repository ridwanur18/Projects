//Name: Ridwanur Rahman
//ID: 260828139

public abstract class Reservation {
	
	private String name;
	
	public Reservation(String name) {
		
		this.name = name;
		
	}
	
	public final String reservationName() {
		
		return this.name;
		
	}
	
	public abstract int getCost();
	
	public abstract boolean equals(Object o);

}
