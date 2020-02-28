import matplotlib.pyplot as plt

left_edges = [0, 10, 20, 30, 40]
heights = [100, 200, 300, 400, 500]
bar_width = 5
plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'm', 'k'))
plt.show()
