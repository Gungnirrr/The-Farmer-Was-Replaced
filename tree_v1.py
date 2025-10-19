clear()
size = get_world_size()
while True:
	for i in range(size):
		for j in range(size):
			if (i + j)  % 2 == 0 :
				if can_harvest():
					harvest()
					plant(Entities.Tree)
			else:
				if can_harvest():
					harvest()
					plant(Entities.Bush)
			move(North)
		move(East)