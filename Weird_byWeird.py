set_world_size(16)
while True:
	clear()
	size = get_world_size()
	for i in range(size):
		for j in range(size):
			if (i + j)  % 2 == 0 :
				if can_harvest():
					harvest()
					plant(Entities.Tree)
					x,y = get_pos_x(),get_pos_y()
					if x % 3 == 0 or y % 3 == 0:
						use_item(Items.Weird_Substance)
			else:
				if can_harvest():
					harvest()
					plant(Entities.Bush)
					x,y = get_pos_x(),get_pos_y()
					if x % 3 == 0 or y % 3 == 0:
						use_item(Items.Weird_Substance)
			move(North)
		move(East)
	size = get_world_size()
	for i in range(size):
		for j in range(size):
			if True:
				if can_harvest():
					harvest()
			move(North)
		move(East)