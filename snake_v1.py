size = get_world_size() 
clear() 

size = 8
set_world_size(8)
body_size = 1
moved = False
def check():
	global apple_x 
	global apple_y
	global body_size
	global moved 
	x,y = get_pos_x(),get_pos_y()
	if x == apple_x and y == apple_y:
		l = measure()
		if l :
			apple_x ,apple_y = l[0],l[1]
			body_size += 1
		else :
			moved = False
def move_and_check(d):
	global moved 
	if	move(d) :
		moved = True
	else:
		moved = False
	check()
	
def move_circle():
	global apple_x 
	global apple_y
	global body_size
	for i in range(size-2):
		move_and_check(North)
		x,y = get_pos_x(),get_pos_y()
		if x == apple_x and y == apple_y:
			l = measure() 
			if l :
				apple_x ,apple_y = l[0],l[1]
				body_size += 1
			else :
				moved = False 
	move_and_check(East)
	x,y = get_pos_x(),get_pos_y()
	if x == apple_x and y == apple_y:
		apple_x ,apple_y = measure()
		body_size += 1
	for i in range(size -2):
		move_and_check(South)
		x,y = get_pos_x(),get_pos_y()
		if x == apple_x and y == apple_y:
			apple_x ,apple_y = measure()
			body_size += 1
def move_all():
	global apple_x 
	global apple_y
	global body_size 
	global moved 
	move_circle()
	x = get_pos_x()
	moved = False
	while (x + 1) * (size -1) < body_size :
		move_and_check(East)
		move_circle()
		x = get_pos_x()
		if x == size -1 :
			move_abs(x,0)
			move_abs(0,0)
			move_abs(0,1)
			return  
		if not moved :
			change_hat(Hats.Brown_Hat)
			return
			#change_hat(Hats.Dinosaur_Hat)
	

	if (x + 1) * (size -1) >= body_size :
		move_and_check(East)
		x,y = get_pos_x(),get_pos_y()
		while apple_x >= x and x != size - 1 :
			if apple_y == 0 :
				if apple_x > x :
					for i in range (apple_x -x):
						move_and_check(East)
				move_and_check(South)
				#apple_x ,apple_y = measure()
				#body_size += 1 
				x,y = get_pos_x(),get_pos_y()
				move_abs(0,0)
				move_abs(0,1)
				return 
			if apple_x >= x :
				x_moved = apple_x - x 
				for i in range(apple_y - y):
					move_and_check(North)
				for i in range(apple_x - x):
					move_and_check(East)
				#apple_x ,apple_y = measure()
				#body_size += 1 
				
				x,y = get_pos_x(),get_pos_y()
				if x_moved > 0 :
					move_abs(x,1)
				if x != size-1:
					move_and_check(East)
			x,y = get_pos_x(),get_pos_y()
			

		move_abs(x,0)
		move_abs(0,0)
		move_abs(0,1)
			 
		
def move_abs(x,y):
	x_,y_ = get_pos_x(),get_pos_y()
	if x_ < x :
		for i in range(x-x_):
			move_and_check(East)
	else:
		for i in range(x_-x):
			move_and_check(West)
	if y_ < y :
		for i in range(y-y_):
			move_and_check(North)
	else:
		for i in range(y_-y):
			move_and_check(South)
def move_abs_not_check(x,y):
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
while True:
	body_size = 1 
	move_abs_not_check(0,1)
	change_hat(Hats.Dinosaur_Hat)
	
	apple_x, apple_y = measure()
	move_abs(0,1)
	while True:
		move_all()
		if not moved:
			break 
