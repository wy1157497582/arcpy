total = 0
def cc(increment):
    global total
    if total:
        total += increment
    else:
        total = increment
    return total
	  
print cc(1)
	  