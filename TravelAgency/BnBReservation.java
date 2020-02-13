//Name: Ridwanur Rahman
//ID: 260828139

public class BnBReservation extends HotelReservation {
	
	public BnBReservation(String name, Hotel h, String type, int nights) {
		
		super(name, h, type, nights);
		h.reserveRoom(type);
		
	}
	
	public int getCost() {
		
		int breakfast = 10*100;
		
		return (super.getCost()) + (breakfast*super.getNumOfNights());
		
	}
	
}
