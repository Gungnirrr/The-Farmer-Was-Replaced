size = get_world_size()
def move_abs1(x,y):
	x_,y_ = get_pos_x(),get_pos_y()
	if x_ < x :
		for i in range(x-x_):
			move(East)
	else:
		for i in range(x_-x):
			move(West)
	if y_ < y :
		for i in range(y-y_):
			move(North)
	else:
		for i in range(y_-y):
			move(South)
size = get_world_size()
def move_abs(x,y):
	if size == 22 :
		return move_abs1(x,y)
	x_,y_ = get_pos_x(),get_pos_y()
	if x_ < x :
		step = x-x_ 
		if step < size - step:
			for i in range(step):
				move(East)
		else:
			for i in range(size - step):
				move(West)
	else:
		step = x_- x
		if step < size - step:
			for i in range(step):
				move(West)
		else:
			for i in range(size - step):
				move(East)
	if y_ < y :
		step = y-y_
		if step < size - step:
			for i in range(step):
				move(North)
		else:
			for i in range(size - step):
				move(South)
	else:
		step = y_-y
		if step < size - step:
			for i in range(step):
				move(South)
		else:
			for i in range(size - step):
				move(North)