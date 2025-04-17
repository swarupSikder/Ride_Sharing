from ride import RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

niye_jao = RideSharing('Niye Jao')

rahim = Rider('Rahim', 'ea@k.com', 1234, 'Mohakhali', 1200)
niye_jao.add_rider(rahim)

kolim = Driver('kolim', 'kolim@k.com', 123123, 'Gulshan')
niye_jao.add_driver(kolim)


rahim.requestRide(niye_jao, "Uttara", 'car')
rahim.show_current_ride()
kolim.reach_destination(rahim.current_ride)
print(niye_jao)