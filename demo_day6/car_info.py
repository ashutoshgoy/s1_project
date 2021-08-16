def car_info(manufacturer,model_name,**other_information):
    car={'maufacturer':manufacturer,'model_name':model_name,'misc_info':other_information}
    return car
#call this car info function with values
#manufacturer=tesla
#model=s
#color=white
#type='sedan'
#vahicle_power=battery
car=car_info(manufacturer='tesla',model_name='s',color='white',type='Sedan',vehicle_power='battery')

for k,v in car[info].items():
