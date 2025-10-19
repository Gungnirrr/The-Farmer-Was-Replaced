while True:
	clear()
	size = get_world_size()
	import f0 
	drons = max_drones()
	if size % drons != 0 :
		size = size - (size % drons)
		set_world_size(size)
	alldrons = []
	for n in range(drons):
		def plant_and_havest():
			while True:
				dead = 0
				for i in range(size/drons):
					for y in range(size):
						x = n * size/drons  +i 
						f0.move_abs(x,y)
						if get_water() < 0.5:
							use_item(Items.Water)
						if get_ground_type() != Grounds.Soil:
							till()
						if not can_harvest():
							harvest()
							dead +=1 
						plant(Entities.Pumpkin)
						#move(North)
				if dead == 0 :
					return 
					#dead = 0 
		d = spawn_drone(plant_and_havest)
		if d :
			alldrons.append(d)
		else:
			plant_and_havest()
	for d in alldrons:
		if not has_finished(d):
			wait_for(d)
	harvest()
		
			