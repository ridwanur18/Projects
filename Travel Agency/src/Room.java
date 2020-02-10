//Name: Ridwanur Rahman
//ID: 260828139

public class Room {

	private String roomType;
	private int price;
	private boolean availability;
	
	public Room(String type) {
		
		this.roomType = type;
		
		if (this.roomType == "double") {
			this.price = 90*100;
		}
		else if (this.roomType == "queen") {
			this.price = 110*100;
		}
		else if (this.roomType == "king") {
			this.price = 150*100;
		}
		else {
			throw new IllegalArgumentException("No such room type can be created, sorry.");
		}
		
		this.availability = true;
	}
		
	public Room(Room r1) {
		
		this.roomType = r1.roomType;
		this.price = r1.price;
		this.availability = r1.availability;
		
	}
	
	public String getType() {
		
		return this.roomType;
		
	}
	
	public int getPrice() {
		
		return this.price;
		
	}
	
	public void changeAvailability() {
		
		this.availability = !this.availability;
		
	}
	
	public static Room findAvailableRoom(Room[] r, String type) {
		
		for (int i=0; i<r.length; i++) {
			if (r[i].availability && r[i].roomType.equalsIgnoreCase(type)) {
				return r[i];
			}
		}
		return null;
		
	}
	
	public static boolean makeRoomAvailable(Room[] r, String type) {
		
		for (int i=0; i<r.length; i++) {
			if (!r[i].availability && r[i].roomType.equalsIgnoreCase(type)) {
				r[i].changeAvailability();
				return true;
			}
		}
		return false;
	}	
	
}
