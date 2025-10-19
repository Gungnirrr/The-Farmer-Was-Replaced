while True:
	clear()
	size = get_world_size()
	import f0 
	f0.move_abs(0,0)
	for x in range (size):
		for y in range(size):
			f0.move_abs(x,y)
			if x % 2 == 0:
				if x % 4 == 0 and y % 3 == 0:
					plant(Entities.Tree)
					use_item(Items.Weird_Substance)
				elif x % 4 != 0 and y % 3 == 1 :
					plant(Entities.Tree)
					use_item(Items.Weird_Substance)
	f0.move_abs(0,0)
	for x in range (size):
		for y in range(size):
			if can_harvest():
				harvest()
			move(North)
		move(East)
	
	 