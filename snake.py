clear() 
change_hat(Hats.Dinosaur_Hat)
import f0 
def move_abs(x,y):
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
	x,y = get_pos_x(),get_pos_y()
	ll = measure()
	if ll == None:
		change_hat(Hats.Brown_Hat)
		change_hat(Hats.Dinosaur_Hat)	 
	next_x,next_y = measure()
	move_abs(next_x,next_y)
	xx,yy = get_pos_x(),get_pos_y()
	if xx == x and yy == y :
		change_hat(Hats.Brown_Hat)
		change_hat(Hats.Dinosaur_Hat)	
		