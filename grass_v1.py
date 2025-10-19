clear()
size = get_world_size()
#size = 3
while True:
	for i in range(size):
		if can_harvest():
			harvest()
			move(North)
	move(East)