import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 3
cost_per_class = cost_per_week / classes_per_week
print("The cost per class is $", cost_per_class)

print(weeks, type(weeks))
print(classes, type(classes))
print(tuition, type(tuition))
print(cost_per_week, type(cost_per_week))
print(classes_per_week, type(classes_per_week))
print(cost_per_class, type(cost_per_class))

#Part B
my_ran_var = [2, "hi", 5.0, 79, "bye"]
the_choice = random.choice(my_ran_var)
print(the_choice)