//Name: Ridwanur Rahman
//ID: 260828139

public class Hotel {
	
	private String hotelName;
	private Room[] room;
	
	public Hotel(String name, Room[] r) {
		
		this.hotelName = name;
		this.room = new Room[r.length];
		for (int i=0; i<r.length; i++) {
			this.room[i] = new Room(r[i]);
		}
		
	}
		
	public int reserveRoom(String type) {
		
		Room roomAvailable = Room.findAvailableRoom(this.room, type);
		if (roomAvailable != null) {
			roomAvailable.changeAvailability();
			return roomAvailable.getPrice();
		}
		else {
			throw new IllegalArgumentException("No room of such type is available.");
		}
		
	}
	
	public boolean cancelRoom(String type) {
		
		if (Room.makeRoomAvailable(this.room, type)) {
			return true;
		}
		return false;
	}
	
}
