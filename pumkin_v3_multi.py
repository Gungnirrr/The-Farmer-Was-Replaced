while True:
	clear()
	size = get_world_size()
	import f0 
	drons = max_drones()
	size = get_world_size()
	if size % drons != 0 :
		size = size - (size % drons)
		set_world_size(size)
	alldrons = []
	for n in range(drons):
		def plant_and_havest():
			d= {} 
			x = n * size/drons
			l = [] 
			for i in range(size):
				d[(x,i)] = False
				l.append((x,i)) 
			#first = True
			for i in range(size/drons):
				for y in range(size):
					x = n * size/drons  +i 
					f0.move_abs(x,y)
					if get_water() < 0.7:
						use_item(Items.Water)
					if get_ground_type() != Grounds.Soil:
						till()
					plant(Entities.Pumpkin)
			for i in range(size/drons):
				for y in range(size):
					x = n * size/drons  +i 
					f0.move_abs(x,y)
					if can_harvest():
						d.pop((x,y))
					elif get_entity_type() == Entities.Dead_Pumpkin:
						harvest()
						plant(Entities.Pumpkin)
			dead = len(d)
			while True :
				poss = [] 
				for i in d :
					poss.append(i)
				for i in poss :
					f0.move_abs(i[0],i[1])
					if can_harvest():
						d.pop(i)
						if len(d) == 0 :
							return 
					elif get_entity_type() == Entities.Dead_Pumpkin:
						harvest()
						plant(Entities.Pumpkin)
					else:
						if get_water() < 0.7:
							use_item(Items.Water)
					
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
		
			