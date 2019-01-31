from myclass import my_point
from myclass import my_point_child

x = my_point(1,2)
y = my_point(5,6)
x.print_ab()
print(x.sum_ab())
print(y.mult_ab())

#child class
z = my_point_child(7, 8, 3)
z.print_ab()
print(z.mult_ab())
print(z.n_square())
z.print_msg()

