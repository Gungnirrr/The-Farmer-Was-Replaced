clear()
size = get_world_size()
import f0 
drons = max_drones()
#set_world_size(16)
#drons = 16
alldrons = []
if size % drons != 0 :
	size = size - (size % drons)
	set_world_size(size)
	
while True:
	for n in range(drons):
		def plant_and_havest():
			for i in range(get_world_size()/drons):
				for y in range(get_world_size()):
					x = n * get_world_size()/drons +i 
					f0.move_abs(x,y)
					if x % 2 == 0:
						if x % 4 == 0 and y % 3 == 0:
							plant(Entities.Tree)
							use_item(Items.Weird_Substance)
							if get_water() < 0.7 :
								use_item(Items.Water)
						elif x % 4 != 0 and y % 3 == 1 :
							plant(Entities.Tree)
							use_item(Items.Weird_Substance)
							if get_water() < 0.7 :
								use_item(Items.Water)
					#move(North)
		d =  spawn_drone(plant_and_havest)
		if d :
			alldrons.append(d)
		else:
			plant_and_havest()
	for d in alldrons:
		wait_for(d)
	for n in range(drons):
		def har():
			for i in range(get_world_size()/drons):
				for y in range(get_world_size()):
					x = n * get_world_size()/drons +i 
					f0.move_abs(x,y)
					while True:
						if can_harvest():
							harvest()
							break 
		d =  spawn_drone(har)
		if d :
			alldrons.append(d)
		else:
			har()

	 