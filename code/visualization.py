import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

# Data for visualization
tools = ["Pandas", "FireDucks"]
times = [pandas_load_time, fireducks_load_time]

# Create a bar chart
fig, ax = plt.subplots()
bar = ax.bar(tools, times, color=["blue", "green"])
ax.set_ylabel("Load Time (sec)")
ax.set_title("Performance Comparison")

# Animation function
def animate(i):
    for rect, h in zip(bar, times[:i+1]):
        rect.set_height(h)
    return bar

ani = FuncAnimation(fig, animate, frames=len(times), interval=1000, repeat=False)
plt.show()

# Save as GIF
ani.save("performance_comparison.gif", writer="imagemagick")