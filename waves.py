import numpy as np
import matplotlib.pyplot as plt

# Function to generate a signal based on amplitude, frequency, phase, and time/distance array
def generate_signal(A, f, phi, t):
    # A: Amplitude of the signal
    # f: Frequency of the signal
    # phi: Phase of the signal
    # t: Time or distance array
    return A * np.sin(2 * np.pi * f * t + phi)

# Read characteristics of the first signal (D1) from the user
A1 = float(input("Enter the amplitude (A) of signal D1: "))
f1 = float(input("Enter the frequency (f) of signal D1: "))
phi1 = float(input("Enter the phase (φ) of signal D1: "))

# Read characteristics of the second signal (D2) from the user
A2 = float(input("Enter the amplitude (A) of signal D2: "))
f2 = float(input("Enter the frequency (f) of signal D2: "))
phi2 = float(input("Enter the phase (φ) of signal D2: "))

# Read the fixed distance (x1) and fixed time (t1) from the user
x1 = float(input("Enter the fixed distance (x1): "))
t1 = float(input("Enter the fixed time (t1): "))

# Generate an array of time values from 0 to 1 second, with 1000 points
t = np.linspace(0, 1, 1000)
# Generate an array of distance values from 0 to 10 meters, with 1000 points
x = np.linspace(0, 10, 1000)

# Generate the first signal (D1) in the time domain at fixed distance x1
D1_time = generate_signal(A1, f1, phi1, t)
# Generate the second signal (D2) in the time domain at fixed distance x1
D2_time = generate_signal(A2, f2, phi2, t)
# Calculate the sum of the two signals in the time domain
sum_time = D1_time + D2_time

# Generate the first signal (D1) in the distance domain at fixed time t1
D1_distance = generate_signal(A1, f1, phi1, x)
# Generate the second signal (D2) in the distance domain at fixed time t1
D2_distance = generate_signal(A2, f2, phi2, x)
# Calculate the sum of the two signals in the distance domain
sum_distance = D1_distance + D2_distance

# Create a figure for plotting with a specified size
plt.figure(figsize=(12, 6))

# Create the first subplot for the time domain signals
plt.subplot(2, 1, 1)
# Plot the first signal (D1) in the time domain
plt.plot(t, D1_time, label='D1')
# Plot the second signal (D2) in the time domain
plt.plot(t, D2_time, label='D2')
# Plot the sum of the two signals in the time domain
plt.plot(t, sum_time, label='Sum')
# Set the title of the subplot
plt.title(f'Signals in Time Domain at Fixed Distance x={x1}')
# Label the x-axis
plt.xlabel('Time (s)')
# Label the y-axis
plt.ylabel('Amplitude')
# Add a legend to the plot
plt.legend()

# Create the second subplot for the distance domain signals
plt.subplot(2, 1, 2)
# Plot the first signal (D1) in the distance domain
plt.plot(x, D1_distance, label='D1')
# Plot the second signal (D2) in the distance domain
plt.plot(x, D2_distance, label='D2')
# Plot the sum of the two signals in the distance domain
plt.plot(x, sum_distance, label='Sum')
# Set the title of the subplot
plt.title(f'Signals in Distance Domain at Fixed Time t={t1}')
# Label the x-axis
plt.xlabel('Distance (m)')
# Label the y-axis
plt.ylabel('Amplitude')
# Add a legend to the plot
plt.legend()

# Adjust the layout to prevent overlap between subplots
plt.tight_layout()
# Display the plots
plt.show()
