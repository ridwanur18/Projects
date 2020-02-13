//Name: Ridwanur Rahman
//ID: 260828139

public class HotelReservation extends Reservation {
	
	private Hotel h;
	private String type;
	private int nights;
	private int price;
	
	public HotelReservation(String name, Hotel h, String type, int nights) {
		
		super(name);
		this.h = h;
		this.type = type;
		this.nights = nights;
		Room room = new Room(type);
		this.price = room.getPrice();
		h.reserveRoom(type);			//Reserves a room of specified type
	}
	
	public int getNumOfNights() {
		
		return this.nights;
		
	}
	
	public int getCost() {
		
		Room room = new Room(type);
		
		return room.getPrice()*getNumOfNights();
		
	}
	
	public boolean equals(Object o) {
		
		if (o instanceof HotelReservation) {
			return ((((HotelReservation) o).type.equalsIgnoreCase(this.type)) && (((HotelReservation) o).reservationName().equalsIgnoreCase(this.reservationName()) && (((HotelReservation) o).nights == (this.nights)) && (((HotelReservation) o).price == (this.price))));
		}
		return false;
		
	}
	
}
