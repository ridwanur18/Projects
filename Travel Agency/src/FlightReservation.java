//Name: Ridwanur Rahman
//ID: 260828139

public class FlightReservation extends Reservation {
	
	private Airport departure;
	private Airport arrival;
	
	public FlightReservation(String name, Airport departure, Airport arrival) {
		
		super(name);
		this.departure = departure;
		this.arrival = arrival;
		
		if (departure.equals(arrival)) {
			throw new IllegalArgumentException("The arrival and departure locations are same.");
		}
	}
	
	public int getCost() {
		
		double distance = Airport.getDistance(this.departure, this.arrival);
		double fuelCost = (distance/167.52) * 124;					
		double airportFees = this.departure.getFees() + this.arrival.getFees();
		double fixedCost = 53.75*100;
		
		double totalCost = fuelCost + airportFees + fixedCost;
		totalCost = Math.ceil(totalCost);
		
		return (int) totalCost;
	}
	
	public boolean equals(Object o) {
		
		if (o instanceof FlightReservation) {
			return ((FlightReservation) o).departure.equals(this.departure) && ((FlightReservation) o).arrival.equals(this.arrival) && ((FlightReservation) o).reservationName().equalsIgnoreCase(this.reservationName());
		}
		return false;
	}
	
}
 