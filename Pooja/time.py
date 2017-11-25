time=input()
if time[-2:]=='AM':
    new=time[:-2]
else:
    new=str(int(time[:2])+12)+time[2:-2]
print(new)
