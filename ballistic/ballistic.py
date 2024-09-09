import numpy as np
import matplotlib.pyplot as plt

# Defining the distance range (in meters) with 50-meter increments
distance = np.arange(0, 1001, 50)

# Defining ballistic coefficients (BC) and muzzle velocities (m/s) for each caliber
calibers = {
    "6.5x55 SE": {"BC": 0.625, "velocity": 820},
    "6.5 Creedmoor": {"BC": 0.625, "velocity": 830},
    "6mm Creedmoor": {"BC": 0.620, "velocity": 900},
    ".243 Win": {"BC": 0.550, "velocity": 950},
    "6 XC": {"BC": 0.620, "velocity": 880},
}

# Air density and gravity (standard conditions)
air_density = 1.225  # kg/m³
g = 9.81  # m/s²


def calculate_ballistics(BC, velocity, distance):
    """Calculate speed and drop over distance given BC, initial velocity, and distance."""
    # Speed decrease model
    speed = velocity * np.exp(-0.000147 * distance / (BC * air_density))

    # Drop calculation using a more straightforward method
    time = distance / ((velocity + speed) / 2)  # average velocity over distance
    drop = 0.5 * g * time ** 2  # free fall equation

    return speed, drop


# Prepare the plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plotting each caliber
for caliber, params in calibers.items():
    speed, drop = calculate_ballistics(params["BC"], params["velocity"], distance)

    # Convert drop from meters to centimeters
    drop_cm = drop * 100

    # Plot speed
    ax1.plot(distance, speed, label=caliber)

    # Plot drop
    ax2.plot(distance, drop_cm, label=caliber)

# Speed plot formatting
ax1.set_title("Speed vs Distance for Various Calibers")
ax1.set_xlabel("Distance (m)")
ax1.set_ylabel("Speed (m/s)")
ax1.set_xticks(distance)  # Set x-ticks to every 50 meters
ax1.grid(True)
ax1.legend()

# Drop plot formatting
ax2.set_title("Bullet Drop vs Distance for Various Calibers")
ax2.set_xlabel("Distance (m)")
ax2.set_ylabel("Bullet Drop (cm)")
ax2.set_xticks(distance)  # Set x-ticks to every 50 meters
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()


# elso = int(input("Elso szam"))
# masodik = int(input("Masodik szam"))
#
# try:
#     valami = elso / masodik
#
# except ValueError:
#     print("Value erro van buzi")
# except ZeroDivisionError:
#     print("Ne akarj nullavalosztani buzi")
# else:
#     print(f"{elso} / {masodik} = {valami}")
# finally:
#     print("Ez meg igy is ugyis lefut")