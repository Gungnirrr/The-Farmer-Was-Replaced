
import f0 
while True:
	drons = max_drones()
	size = get_world_size() 
	if size % drons != 0 :
		size = size - (size % drons)
		set_world_size(size)
	def sort_x(x,size):
		for i in range(size):
			for j in range(0,size-i-1):
				f0.move_abs(x,j)
				#print(x,j,i)
				if measure() > measure(North):
					swap(North)
	def sort_y(y,size):
		for i in range(size):
			for j in range(0,size-i-1):
				f0.move_abs(j,y)
				#print(x,j,i)
				if measure() > measure(East):
					swap(East)
			
	clear()
	f0.move_abs(0,0)
	size = get_world_size() 
	alldrons = []
	for n in range(drons):
		def plant_cactus():
			for i in range(get_world_size()/drons):
				for y in range(get_world_size()):
					x = n * get_world_size()/drons +i 
					f0.move_abs(x,y)
					if get_water() < 0.25:
						use_item(Items.Water)
					if get_ground_type() != Grounds.Soil:
						till()
					if can_harvest():
						harvest()
					plant(Entities.Cactus)
		d =  spawn_drone(plant_cactus)
		if d :
			alldrons.append(d)
		else:
			plant_cactus()
		#print(num_drones(),max_drones())
	for d in alldrons:
		if not has_finished(d):
			wait_for(d)
	alldrons = []
	drons = max_drones()
	for x in range(drons):
		def sort():
			for i in range(size/drons):
				sort_x(x * get_world_size()/drons + i,size)
		d =  spawn_drone(sort)
		if d :
			alldrons.append(d)
		else:
			sort()
		#while True:
			#if spawn_drone(sort):
				#break
	for d in alldrons:
		if not has_finished(d):
			wait_for(d)
	alldrons = []		
	for y in range(drons):
		def sort():
			for i in range(size/drons):
				sort_y(y * get_world_size()/drons + i,size)
		#def sort():
			#sort_y(y,size)
		d =  spawn_drone(sort)
		if d :
			alldrons.append(d)
		else:
			sort()
		#while True:
			#if spawn_drone(sort):
			#	break
	for d in alldrons:
		if not has_finished(d):
			wait_for(d)
	alldrons = []		
	harvest()
	