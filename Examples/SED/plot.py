import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# ---------------------- Parameters ----------------------
fig = plt.figure(figsize=(20, 4))

NQPOINTS = 26       # Total number of Q points
NE = 4096           # Number of energy points per SQE file

vmin, vmax = 2, 5.0
EMAX = 20

ymajor, yminor = 5, 1

# High-symmetry points
xl = np.array([0.5, 10.5, 20.5, 25.5])
my_xticks = ["$\Gamma$", "M", "$\Gamma$", "A"]

# Data containers
SQE = np.zeros((NQPOINTS, NE))

elements = ["Li", "O", "Al", "Si",'Total']
file_list = ["SEDTOTAL"]

# ---------------------- Main Loop ----------------------
kk = 0
for filename in file_list:
    data = np.loadtxt(filename)
    ylim = np.max(data[:, 0])

    for l in range(1, 6):
        kk += 1
        ax = fig.add_subplot(1, 5, kk)

        # Title
        ax.set_title(f"{elements[l-1]}")

        # Extract SQE
        for i in range(NQPOINTS):
            SQE[i, :] = data[i * NE:(i + 1) * NE, l]

        # Rotate + log scale
        temp = np.rot90(np.log10(SQE), 1)

        # Plot
        im = ax.imshow(
            temp,
            aspect='auto',
            cmap='viridis',
            vmin=vmin,
            vmax=vmax,
            extent=[0, NQPOINTS, 0, ylim],
            interpolation='nearest'
        )

        # Axes formatting
        ax.set_xticks(xl)
        ax.set_xticklabels(my_xticks, fontsize=16)
        ax.set_ylim(0, EMAX)

        if kk == 1:
            ax.set_ylabel('Energy (meV)', fontsize=20)

        ax.tick_params(axis='both', which='both', labelsize=16, width=1)
        ax.tick_params(which='major', length=8)
        ax.tick_params(which='minor', length=4)

        ax.yaxis.set_major_locator(MultipleLocator(ymajor))
        ax.yaxis.set_minor_locator(MultipleLocator(yminor))

# ---------------------- Layout & Save ----------------------
plt.subplots_adjust(
    left=0.15, right=0.90,
    bottom=0.10, top=0.95,
    wspace=0.4, hspace=0.4
)

plt.savefig('SED.png', bbox_inches="tight", dpi=600)
plt.show()
