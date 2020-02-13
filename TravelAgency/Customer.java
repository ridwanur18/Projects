//Name: Ridwanur Rahman
//ID: 260828139

public class Customer {
	
	private String customerName;
	private int customerBalance;
	private Basket resBasket;
	
	public Customer(String name, int balance) {
		
		this.customerName = name;
		this.customerBalance = balance;
		this.resBasket = new Basket();
		
	}
	
	public String getName() {
		
		return this.customerName;
		
	}
	
	public int getBalance() {
		
		return this.customerBalance;
		
	}
	
	public Basket getBasket() {
		
		return this.resBasket;
		
	}
	
	public int addFunds(int toAdd) {
		
		if (toAdd < 0) {
			throw new IllegalArgumentException("Balance to add cannot be negative.");
		}
		else {
			this.customerBalance += toAdd;
		}
		return this.customerBalance;
	}
	
	public int addToBasket(Reservation r) {
		
		 if (r.reservationName().equalsIgnoreCase(this.customerName)) {
			 this.resBasket.add(r);
			 return this.resBasket.getNumOfReservations();
		 }
		 else {
			 throw new IllegalArgumentException("This reservation is made by a different customer.");
		 }
		
	}
	
	public int addToBasket(Hotel h, String roomType, int numOfNights, boolean breakfast) {
		
		HotelReservation hotelres = new HotelReservation(this.customerName, h, roomType, numOfNights);
		resBasket.add(hotelres);
		
		return this.resBasket.getNumOfReservations();
		
	}
	
	public int addToBasket(Airport a1, Airport a2) {
		
		FlightReservation flightres = new FlightReservation(this.customerName, a1, a2);
		resBasket.add(flightres);
		
		return this.resBasket.getNumOfReservations();
		
	}
	
	public boolean removeFromBasket(Reservation r) {
		
		return resBasket.remove(r);
		
	}
	
	public int checkOut() {
		
		if (this.customerBalance < resBasket.getTotalCost()) {
			throw new IllegalStateException("Customer balance is not enough to cover total cost of their basket.");
		}
		else {
			this.customerBalance = this.customerBalance - resBasket.getTotalCost();
			resBasket.clear();
			return this.customerBalance;
		}
		
	}
	
}
