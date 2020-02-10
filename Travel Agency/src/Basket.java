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
			for (int i=0; i<this.reservations.length; i++) {
				if (this.reservations[i].equals(r) && this.reservations[i].reservationName().equalsIgnoreCase(r.reservationName())) {
					Reservation[] newReservations = new Reservation[this.reservations.length-1];
					int index = i;
					
					for (int j=0; j<this.reservations.length; i++) {
						if (j == index) {
							continue;
						}
						else {
							newReservations[j] = this.reservations[j];
						}
					}
					return true;
				}
			}
		}
		return false;
	}
	
	public void clear() {
		
		for (int i=0; i<this.reservations.length; i++) {
			this.reservations[i] = null;
		}
		
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
