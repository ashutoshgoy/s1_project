cars = {
'bmw': 'germany',
'suzuki': 'japan',
'mercedes': 'germany',
'porsche': 'germany',
'tesla': 'usa',
'ferrari': 'italy'

}
countries=['usa','japan','italy']

for car_brand,country in cars.items():
     if  country in countries:
         print(car_brand)


