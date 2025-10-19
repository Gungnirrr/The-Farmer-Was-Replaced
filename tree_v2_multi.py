clear()
size = get_world_size()
import f0 
drons = max_drones()
alldrons = []
if size % drons != 0 :
	size = size - (size % drons)
	set_world_size(size)
for n in range(drons):
	def plant_and_havest():
		while True:
			for i in range(get_world_size()/drons):
				for y in range(get_world_size()):
					x = n * get_world_size()/drons +i 
					f0.move_abs(x,y)
					if get_water() < 0.25:
						use_item(Items.Water)
					if (x + y)  % 2 == 0 :
						if can_harvest():
							harvest()
							plant(Entities.Tree)
					else:
						if can_harvest():
							harvest()
							plant(Entities.Bush)
					#move(North)
	d =  spawn_drone(plant_and_havest)
	if d :
		alldrons.append(d)
	else:
		plant_and_havest()
	
			