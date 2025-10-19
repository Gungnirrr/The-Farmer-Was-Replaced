clear()
size = get_world_size()
while True:
	dead = 0
	for i in range(size):
		for j in range(size):
			if get_ground_type() != Grounds.Soil:
				till()
			if not can_harvest():
				harvest()
				dead +=1 
				
			#if can_harvest():
			#	harvest()
			plant(Entities.Pumpkin)
			move(North)
		move(East)
	if dead == 0 :
		harvest()
		dead = 0 
	