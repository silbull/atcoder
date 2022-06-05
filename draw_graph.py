import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates

cach_size_x = [8, 16, 32, 64, 128, 256]
way_x = [1, 2, 4, 8, 16, 32]

#連想度1
ac_time_1 = [1.09423, 1.18257, 1.26867, 1.63961, 1.82145, 1.91286]
ene_1 = [0.018999, 0.0332744, 0.0634321, 0.0895717, 0.117374, 0.224793] 

#連想度2
ac_time_2 = [1.17962, 1.18269, 1.2689, 1.64004, 1.82155, 1.91445]
ene_2 = [0.0306886, 0.0331129, 0.0626449, 0.0877196, 0.115611, 0.226726]

#連想度4
ac_time_4 = [1.24238, 1.3755, 1.26907, 1.64166, 1.82313, 1.91442]
ene_4 = [0.0361295, 0.0375326, 0.0621026, 0.0892139, 0.11724, 0.223172]

#連想度8
ac_time_8 = [1.32535, 1.4566, 1.47944, 1.69967, 1.82933, 1.9206]
ene_8 = [0.0799829, 0.0817037, 0.0911486, 0.0948224, 0.12075, 0.226472]

#連想度16
ac_time_16 = [1.34611, 1.4301, 1.56138, 1.56806, 1.78839, 1.93748]
ene_16 = [0.1673, 0.168929, 0.171257, 0.17414, 0.179285, 0.235864]

#連想度32
ac_time_32 = [None, 1.48129, 1.56544, 1.6969, 1.92232, 1.92442]
ene_32 = [None, 0.343944, 0.346658, 0.350098, 0.357693, 0.362978]

fig_way, ax1 = plt.subplots( )
fig_way.suptitle("32-way")
ax1.set_xlabel("Cache Size [KB]")
ax1.set_xticks(cach_size_x)

ax1.plot(cach_size_x, ac_time_32, linestyle='dashed', marker='o', label='Access Time')
ax1.set_ylabel("Access Time [ns]")

ax2 = ax1.twinx()
ax2.plot(cach_size_x, ene_32, color='#ff0000', linestyle='dashed', marker='o', label='Read Energy')
ax2.set_ylabel("Read Energy (nJ)")

fig_way.legend(loc='upper left')
plt.savefig('32way_graph.png')



fig_cache, ax3 = plt.subplots( )
fig_cache.suptitle("Cache Size = 256 [KB]")
ax3.set_xlabel("way")
ax3.set_xticks(way_x)

ax3.plot(way_x, [ac_time_1[5], ac_time_2[5], ac_time_4[5], ac_time_8[5], ac_time_16[5], ac_time_32[5]], linestyle='dashed', marker='o', label='Access Time')
ax3.set_ylabel("Access Time [ns]")

ax4 = ax3.twinx()
ax4.plot(way_x, [ene_1[5], ene_2[5], ene_4[5], ene_8[5], ene_16[5], ene_32[5]], color='#ff0000', linestyle='dashed', marker='o', label='Read Energy')
ax4.set_ylabel("Read Energy (nJ)")

fig_cache.legend(loc='upper left')
plt.savefig('size256_graph.png')

#plt.show()
