import sys
import matplotlib.pyplot as plt
import numpy as np

# Load data
loss = np.loadtxt('loss.out')
energy_data = np.loadtxt('energy_train.out')
force_data = np.loadtxt('force_train.out')
#virial_data = np.loadtxt('virial_train.out')
stress_data = np.loadtxt('stress_train.out')

# Function to calculate RMSE
def calculate_rmse(pred, actual):
    return np.sqrt(np.mean((pred - actual) ** 2))

# Create a subplot with 2 row and 2 columns
fig, axs = plt.subplots(2, 2, figsize=(9, 7), dpi=100)

# Plotting the loss figure
axs[0, 0].loglog(loss[:, 1:7], '-', linewidth=2)
axs[0, 0].set_xlabel('Generation', fontsize=10)
axs[0, 0].set_ylabel('Loss functions', fontsize=10)
axs[0, 0].tick_params(axis='both', labelsize=10)
axs[0, 0].legend(['Total', 'L1-Reg', 'L2-Reg', 'Energy-train', 'Force-train', 'Virial-train'], prop = {'size':8})
axs[0, 0].axis('tight')
axs[0, 0].text(-0.07, 1.03, "(a)", transform=axs[0, 0].transAxes, fontsize=12, va='top', ha='right')


# Plotting the energy_data figure
axs[0, 1].plot(energy_data[:, 1], energy_data[:, 0], '.', markersize=10)
axs[0, 1].plot(np.arange(np.min(energy_data[:, 1]), np.max(energy_data[:, 1]), 0.01), np.arange(np.min(energy_data[:, 1]), np.max(energy_data[:, 1]), 0.01), linewidth=2, color='grey', linestyle='--')
axs[0, 1].set_xlabel('DFT energy (eV/atom)', fontsize=10)
axs[0, 1].set_ylabel('NEP energy (eV/atom)', fontsize=10)
axs[0, 1].tick_params(axis='both', labelsize=10)
axs[0, 1].legend(['energy'])
axs[0, 1].axis('tight')

# Calculate and display RMSE for energy
energy_rmse = calculate_rmse(energy_data[:, 0], energy_data[:, 1]) * 1000
axs[0, 1].text(0.5, 0.08, f'RMSE: {energy_rmse:.2f} meV/atom', transform=axs[0, 1].transAxes, fontsize=10, verticalalignment='center')
axs[0, 1].text(-0.07, 1.03, "(b)", transform=axs[0, 1].transAxes, fontsize=12, va='top', ha='right')

# Plotting the force_data figure
axs[1, 0].plot(force_data[:, 3:6], force_data[:, 0:3], '.', markersize=10)
axs[1, 0].plot(np.arange(np.min(force_data[:, 3:6]), np.max(force_data[:, 3:6]), 0.01), np.arange(np.min(force_data[:, 3:6]), np.max(force_data[:, 3:6]), 0.01), linewidth=2, color='grey', linestyle='--')
axs[1, 0].set_xlabel('DFT force (eV/$\AA$)', fontsize=10)
axs[1, 0].set_ylabel('NEP force (eV/$\AA$)', fontsize=10)
axs[1, 0].tick_params(axis='both', labelsize=10)
axs[1, 0].legend(['fx', 'fy', 'fz'])
axs[1, 0].axis('tight')

# Calculate and display RMSE for forces
force_rmse = [calculate_rmse(force_data[:, i], force_data[:, i + 3]) for i in range(3)]
mean_force_rmse = np.mean(force_rmse) * 1000
axs[1, 0].text(0.5, 0.08, f'RMSE: {mean_force_rmse:.2f} meV/$\AA$', transform=axs[1, 0].transAxes, fontsize=10, verticalalignment='center')
axs[1, 0].text(-0.07, 1.03, "(c)", transform=axs[1, 0].transAxes, fontsize=12, va='top', ha='right')

# Plotting the stress figure
axs[1, 1].plot(stress_data[:, 6:12], stress_data[:, 0:6], '.', markersize=10)
axs[1, 1].plot(np.arange(np.min(stress_data[:, 6:12]), np.max(stress_data[:, 6:12]), 0.01), np.arange(np.min(stress_data[:, 6:12]), np.max(stress_data[:, 6:12]), 0.01), linewidth=2, color='grey', linestyle='--')
axs[1, 1].set_xlabel('DFT stress (GPa)', fontsize=10)
axs[1, 1].set_ylabel('NEP stress (GPa)', fontsize=10)
axs[1, 1].tick_params(axis='both', labelsize=10)
axs[1, 1].legend(['xx', 'yy', 'zz', 'xy', 'yz', 'zx'])
axs[1, 1].axis('tight')

# Calculate and display RMSE for stresses
stress_rmse = [calculate_rmse(stress_data[:, i], stress_data[:, i + 6]) for i in range(6)]
mean_stress_rmse = np.mean(stress_rmse) 
axs[1, 1].text(0.5, 0.08, f'RMSE: {mean_stress_rmse:.4f} GPa', transform=axs[1, 1].transAxes, fontsize=10, verticalalignment='center')
axs[1, 1].text(-0.07, 1.03, "(d)", transform=axs[1, 1].transAxes, fontsize=12, va='top', ha='right')

# Adjust layout for better spacing
#plt.tight_layout()
fig.subplots_adjust(top=0.968,bottom=0.088,left=0.086,right=0.983,hspace=0.22,wspace=0.24)

if len(sys.argv) > 1 and sys.argv[1] == 'save':
    plt.savefig('train.png')
else:
    plt.show()
