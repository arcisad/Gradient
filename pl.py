from matplotlib import pyplot as pl
import statistics

num = []
z = []
vent = []
zplus = []
norvent = []
sdv = []
outlier = [0] * 101
temp_norvent = []

with open('units.txt', 'r') as f:
    for line in f:
        data = line.split()
        num.append(int(data[0]))
        z.append(float(data[1]))
with open('flows.txt', 'r') as f2:
    for line in f2:
        data = line.split()
        vent.append(float(data[0]))
l = len(z)
mi = min(z)
ma = max(z)
for i in range(0, l):
    zplus.append(100*(z[i]-mi)/(ma-mi))

for i in range(0, 101):
    match = [x for x in zplus if x >= i and x <= i+1]
    venti = []
    for j in range(0, len(match)):
        matchf = zplus.index(match[j])
        venti.append(vent[matchf])
    if len(venti) == 0:
        ave = 0
        sd = 0
        outlier[i] = 1
    else:
        if len(venti) == 1:
            sd = 0
        else:
            sd = statistics.stdev(venti)
        ave = statistics.mean(venti)
    norvent.append(ave)
    sdv.append(sd)
    if outlier[i] != 1:
        temp_norvent.append(ave)

med = statistics.mean(temp_norvent)
new_norvent = [x / abs(med) for x in norvent]
new_sdv = [x / abs(med) for x in sdv]
print(med)
print(new_norvent)

min_lim = min([x/abs(med) for x in temp_norvent]) - 0.1
max_lim = max([x/abs(med) for x in temp_norvent]) + 0.1

for i in range(0, len(outlier)):
    if outlier[i] == 1:
        new_norvent[i] -= abs(min_lim) + 0.1

ones = [(med/abs(med)) * 1] * 100
pl.hold('on')
pl.xlim([min_lim, max_lim])
pl.plot(ones, range(1, 101), '--')
pl.errorbar(new_norvent, range(0, 101), xerr=new_sdv, fmt='o')
pl.xlabel('normal flow (ml/s)')
pl.ylabel('lung height (%)')
print(med, min(new_norvent), max(new_norvent), sum(new_norvent), sum(vent))
pl.show()

