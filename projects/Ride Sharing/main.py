from ride import calculate_fare, Ride, RideMatching, RideRequest, RideSharing
from user import Rider, Driver
from vehicle import Car, Bike


class MainApp:
	def __init__(self):
		self.pathao = RideSharing("Pathao")
		self.rahim = Rider("Rahim Khan", "rahim@gmail.com", 1395759, "Dhanmondi", 700)
		self.karim = Driver("Karim miya", "karim@gmail.com", 917450, "Mohammadpur")
		self.sakib = Rider("Sakib Hasan", "sakib@gmail.com", 1122334, "Mirpur", 500)
		self.raju = Driver("Raju Ahmed", "raju@gmail.com", 4455667, "Bashundhara")

	def setup(self):
		self.pathao.add_rider(self.rahim)
		self.pathao.add_rider(self.sakib)
		self.pathao.add_driver(self.karim)
		self.pathao.add_driver(self.raju)

	def show_company_info(self):
		print(self.pathao)

	def show_profiles(self):
		self.rahim.display_profile()
		self.karim.display_profile()
		self.sakib.display_profile()
		self.raju.display_profile()

	def show_vehicle_info(self):
		car = Car("car", "A1495VB", 150)
		bike = Bike("bike", "MB2582", 100)
		print(f"Car type: {car.vehicle}, license: {car.license_plate}, rate: {car.rate}")
		print(f"Bike type: {bike.vehicle}, license: {bike.license_plate}, rate: {bike.rate}")
		print(f"Car speed: {Car.speed['car']} km/h")
		print(f"Bike speed: {Bike.speed['bike']} km/h")

	def show_wallet_and_location_features(self):
		self.rahim.load_cash(300)
		self.rahim.update_location("Gulshan")
		self.sakib.load_cash(200)
		self.sakib.update_location("Banani")
		print(f"Rahim wallet: {self.rahim.wallet}, location: {self.rahim.current_location}")
		print(f"Sakib wallet: {self.sakib.wallet}, location: {self.sakib.current_location}")

	def complete_car_ride(self):
		self.rahim.request_ride(self.pathao, "Uttara", "car")
		self.rahim.show_current_ride()
		self.karim.reach_destination(self.rahim.current_ride)
		print(f"Rahim wallet after ride: {self.rahim.wallet}")
		print(f"Karim wallet after ride: {self.karim.wallet}")

	def complete_bike_ride(self):
		self.sakib.request_ride(self.pathao, "Mohakhali", "bike")
		self.sakib.show_current_ride()
		self.raju.reach_destination(self.sakib.current_ride)
		print(f"Sakib wallet after ride: {self.sakib.wallet}")
		print(f"Raju wallet after ride: {self.raju.wallet}")

	def show_fare_demo(self):
		print(f"Fare for 8 km car ride: {calculate_fare(8, 'car')}")
		print(f"Fare for 8 km bike ride: {calculate_fare(8, 'bike')}")

	def run(self):
		self.setup()
		self.show_company_info()
		self.show_profiles()
		self.show_vehicle_info()
		self.show_wallet_and_location_features()
		self.show_fare_demo()
		self.complete_car_ride()
		self.complete_bike_ride()


if __name__ == "__main__":
	app = MainApp()
	app.run()

 