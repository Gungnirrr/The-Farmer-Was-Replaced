size = get_world_size()
while True:
	for i in range(size):
		if can_harvest():
			harvest()
			plant(Entities.Bush)
			move(North)
	move(East)