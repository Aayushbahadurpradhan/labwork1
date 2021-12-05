 # You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
# of the 10 stops on the way. How long will the bus journey take? Alternatively, you could
# run to university. You jog the first mile at 7mph; then run the next two at15mph; before
# jogging the last at 7mph again. Will this be quicker or slower than the bus?
distance = 4
speed_a = 25
stopt = 10*2
time = 1/speed_a
a = time*60
total_time = a+stopt
print(f"the total time to reach university by bus{total_time}")

speed_b = 7
timea = 1/speed_b
time_a = timea*60
speed_c = 15
timeb = 2/speed_c
time_b = timeb*60
speed4 = 7
timec = 1/speed4
time_c = timec*60
total_time_a = time_a+time_b+time_c
print(f"the total time foe walking is {total_time_a}")

if total_time_a>total_time:
    print(f"walking is faster to reach university")