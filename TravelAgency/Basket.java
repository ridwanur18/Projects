//Name: Ridwanur Rahman
//ID: 260828139

public class Basket {
	
	private Reservation[] reservations;
	
	public Basket() {
		
		this.reservations = new Reservation[0];
		
	}
	
	public Reservation[] getProducts() {
		
		return this.reservations;
		
	}
	
	public int add(Reservation r) {
		
		Reservation[] newReservations = new Reservation[this.reservations.length+1];
		
		for (int i=0; i<newReservations.length-1; i++) {
			newReservations[i] = this.reservations[i];
		}
		newReservations[newReservations.length-1] = r;
		
		this.reservations = newReservations;
		
		return newReservations.length;
	}
	
	public boolean remove(Reservation r) {
		
		if (this.reservations.length == 0) {
			return false;
		}
		else {
			Reservation[] newReservations = new Reservation[this.reservations.length-1];
			int index = -1;
			for (int i=0; i<this.reservations.length; i++) {
				
				if (this.reservations[i].equals(r) && this.reservations[i].reservationName().equalsIgnoreCase(r.reservationName())) {
					index = i;
					
				}
			}
			if (index >= 0) {
				
				for (int i=0; i<this.reservations.length; i++) {
					
					if (i < index) {
						newReservations[i] = reservations[i];
					} 
					else if (i == index) {
						continue;
					} 
					else {
						newReservations[i-1] = reservations[i];
					}
				}
				
				this.reservations = newReservations;
				return true;
				
			} 
			else {
				return false;
			}
		}
					
	}
	
	public void clear() {
		
		this.reservations = new Reservation[0];
		
	}
	
	public int getNumOfReservations() {
		
		return this.reservations.length;
		
	}
	
	public int getTotalCost() {
		
		int cost = 0;
		for (int i=0; i<this.reservations.length; i++) {
			cost += this.reservations[i].getCost();
		}
		return cost;
		
	}
	
}
