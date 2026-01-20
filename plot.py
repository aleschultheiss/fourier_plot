import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# x-Achse
x = np.linspace(-2*np.pi, 2*np.pi, 3000)

y_original = np.abs(np.sin(x))

def fourier_abs_sin(x, n_terms):
    result = 2 / np.pi
    for k in range(1, n_terms + 1):
        result -= (4 / np.pi) * np.cos(2 * k * x) / (4 * k**2 - 1)
    return result

n_init = 1
y_fourier = fourier_abs_sin(x, n_init)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

line_original, = ax.plot(x, y_original, label="|sin(x)|", linewidth=2)
line_fourier, = ax.plot(x, y_fourier, label="Fourier-Approximation", linestyle="--")

ax.set_title("Fourier-Reihe von |sin(x)|")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid()

ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(
    ax=ax_slider,
    label="Anzahl Terme n",
    valmin=1,
    valmax=50,
    valinit=n_init,
    valstep=1
)

def update(val):
    n = int(slider.val)
    line_fourier.set_ydata(fourier_abs_sin(x, n))
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()