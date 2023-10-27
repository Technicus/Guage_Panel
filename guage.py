# import matplotlib

# print("Matplotlib Version : {}".format(matplotlib.__version__))


import matplotlib.pyplot as plt


colors = ['#4dab6d', "#72c66e", "#c1da64", "#f6ee54", "#fabd57", "#f36d54", "#ee4d55"]
#
# values = [100,80,60,40,20,0,-20, -40]
values = [100,80,60,40,20,0]

# x_axis_vals = [0, 0.44, 0.88,1.32,1.76,2.2,2.64]
x_axis_vals = [0, 0.44, 0.88,1.32,1.76]

fig = plt.figure(figsize=(18,18))

ax = fig.add_subplot(projection="polar");

# ax.bar(x=[0, 0.44, 0.88,1.32,1.76,2.2,2.64], width=0.5, height=0.5, bottom=2,
ax.bar(x=[0, 0.44, 0.88,1.32,1.76], width=0.5, height=0.5, bottom=2,
# ax.bar(x=[0, 0.44, 0.88,1.32,1.76], width=0.5, height=0.5, bottom=1,
       linewidth=3, edgecolor="white",
       color=colors, align="edge");

# plt.annotate("High Performing", xy=(0.16,2.1), rotation=-75, color="white", fontweight="bold");
# plt.annotate("Sustainable", xy=(0.65,2.08), rotation=-55, color="white", fontweight="bold");
# plt.annotate("Maturing", xy=(1.14,2.1), rotation=-32, color="white", fontweight="bold");
# plt.annotate("Developing", xy=(1.62,2.2), color="white", fontweight="bold");
# plt.annotate("Foundational", xy=(2.08,2.25), rotation=20, color="white", fontweight="bold");
# plt.annotate("Volatile", xy=(2.46,2.25), rotation=45, color="white", fontweight="bold");
# plt.annotate("Unsustainable", xy=(3.0,2.25), rotation=75, color="white", fontweight="bold");

# for loc, val in zip([0, 0.44, 0.88,1.32,1.76,2.2,2.64, 3.14], values):
for loc, val in zip([0, 0.44, 0.88,1.32,1.76,2.2], values):
    plt.annotate(val, xy=(loc, 2.5), ha="right" if val<=20 else "left");

# plt.annotate("50", xytext=(0,0), xy=(1.1, 2.0),
# plt.annotate(" ", xytext=(0,0), xy=(1.57 * 2, 2.0),
plt.annotate(" ", xytext=(0,0), xy=(0 * 2 + 1.57 * 3, 2.0),
# plt.annotate("50", xytext=(0,0), xy=(0.0, 2.0),
             # arrowprops=dict(arrowstyle="wedge, tail_width=0.5", color="black", shrinkA=0),
             arrowprops=dict(arrowstyle="wedge, tail_width=0.25", color="purple", shrinkA=0),
             # bbox=dict(boxstyle="circle", facecolor="black", linewidth=2.0, ),
             bbox=dict(boxstyle="circle", facecolor="black", linewidth=1.0, ),
             # fontsize=45, color="white", ha="center"
             fontsize=25, color="white", ha="center"
            );


plt.title("Performance Gauge Chart", loc="center", pad=20, fontsize=35, fontweight="bold");

# ax.set_axis_off();

plt.show()