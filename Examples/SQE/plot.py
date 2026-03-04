import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# -------------------------------
# Parameters
# -------------------------------
NQPOINTS = 41      # Total number of Q points
NE = 4096          # Number of energy points per SQE file

VMIN = 1
VMAX = 4
EMAX = 15

Y_MAJOR = 5
Y_MINOR = 1

# High symmetry points
xticks_pos = [0,20,41]
xticks_lab = [0,1,2]

#xticks_lab = [r"$\Gamma$", "H", "P", "PA", "N", r"$\Gamma$"]

#ax.set_xticks(xticks_pos)
#ax.set_xticklabels(xticks_lab, fontsize=16)
labels = ['F', 'Ca', 'Zr', 'Total']

# Text location
x_text = 30
y_text = 24

# Input files
file_list = ['SQETOTAL']
path = './'

# -------------------------------
# Arrays
# -------------------------------
SQE = np.zeros((NQPOINTS, NE))

# -------------------------------
# Plot
# -------------------------------
fig = plt.figure(figsize=(8, 12))
subplot_index = 0

for file_name in file_list:

    data = np.loadtxt(path + file_name)
    ylim = np.max(data[:, 0])

    subplot_index += 1
    ax = fig.add_subplot(1, 1, subplot_index)

    # Fill SQE matrix
    for i in range(NQPOINTS):
        SQE[i, :] = np.abs(data[i * NE:(i + 1) * NE, 1])

    # Rotate for plotting
    temp = np.rot90(np.log10(SQE), 1)

    # Plot
    im = ax.imshow(
        temp,
        aspect='auto',
        cmap='viridis',
        vmin=VMIN,
        vmax=VMAX,
        extent=[0, NQPOINTS, 0, ylim],
        interpolation='none'
    )

    # Axis formatting
    ax.set_ylim(0, EMAX)
    ax.set_ylabel('Energy (meV)', fontsize=20)
    ax.set_xlabel('(HH3)', fontsize=20)

    ax.set_xticks(xticks_pos)
    ax.set_xticklabels(xticks_lab, fontsize=16)

    ax.tick_params(which='both', labelsize=16, width=1)
    ax.tick_params(which='major', length=8)
    ax.tick_params(which='minor', length=4)

    ax.yaxis.set_major_locator(MultipleLocator(Y_MAJOR))
    ax.yaxis.set_minor_locator(MultipleLocator(Y_MINOR))

    # Colorbar
    cb = plt.colorbar(im)
    cb.ax.tick_params(labelsize=12)

    # Label
    ax.text(x_text, y_text, labels[0], fontsize=16, color='white', weight='bold')

plt.subplots_adjust(wspace=0.35, hspace=0.40)

plt.savefig('figure.png', dpi=600, bbox_inches="tight")
plt.show()
