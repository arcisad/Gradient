from matplotlib import pyplot as pl
import statistics

num = []
z = []
vent = []
zplus = []
norvent = []
sdv = []


with open('units.txt', 'r') as f:
    for line in f:
        data = line.split()
        num.append(int(data[0]))
        z.append(float(data[1]))
        # z.append(abs(float(data[1])))
with open('flows.txt', 'r') as f2:
    for line in f2:
        data = line.split()
        vent.append(float(data[0]))
        #vent.append((float(data[1])/1000) - (0.85 / 30895))
        #vent.append((float(data[2])))
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
    else:
        if len(venti) == 1:
            sd = 0
        else:
            sd = statistics.stdev(venti)
        ave = statistics.mean(venti)
    norvent.append(ave)
    #print(norvent)
    sdv.append(sd)
temp_norvent = [x for x in norvent if x > 0]
med = statistics.mean(temp_norvent)
new_norvent = [x / med for x in norvent]
new_sdv = [x / med for x in sdv]
#aver=3.59190
print(med)
print(new_norvent)

#ones = [med] * 100
ones = [1] * 100
pl.hold('on')
#pl.plot(norvent, range(0,101),'o')
pl.xlim([0.6, 1.3])
#pl.xlim([0.2, 0.3])
pl.plot(ones, range(1, 101), '--')
pl.errorbar(new_norvent, range(0, 101), xerr=new_sdv, fmt='o')
#pl.errorbar(norvent, range(0, 101), xerr=sdv, fmt='o')
#pl.plot(vent, zplus,'.')
pl.xlabel('normal flow (ml/s)')
#pl.xlabel('Unit Pressure')


#pl.xlabel('Unit volume')
pl.ylabel('lung height (%)')
#pl.text(-6.5, 90,  med)
#pl.plot(vent,zplus,'.')
print(med, min(new_norvent), max(new_norvent), sum(new_norvent), sum(vent))
pl.show()

