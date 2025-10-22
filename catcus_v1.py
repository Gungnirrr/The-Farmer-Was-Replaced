import f0 

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
while True:
	f0.move_abs(0,0)
	size = get_world_size() 
	for x in range(size):
		for y in range(size):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)
			move(North)
		move(East)
	
	for x in range(size):
		sort_x(x,size)
		#spawn_drone(sort_x,x,size)
	for y in range(size):
		sort_y(y,size)
	harvest()
