import time

print("Auto Beat Angle Maker for Custom ADOFAI map")


bpm=int(input("Input the BPM of Song"))
rps=1/(bpm/60)
print("{:.3f}".format(float(rps)))