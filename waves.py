from numpy import ndarray, sin, pi, float64, linspace
import matplotlib.pyplot as plt

def wave(amplitude: float, frequency: float, phase: float, time, distance) -> float64:
    # time or distance, one is an ndarray, while the other is a float
    # D(x,t) = A sin(kx ± ωt + φ̻ )

    if 0 > phase or phase > 2 * pi:
        raise ValueError("phase must be between 0 and 2pi")
    if amplitude == 0:
        raise ValueError("amplitude cannot be 0")
    if frequency < 0:
        raise ValueError("frequency must be greater than 0")

    angular_velocity = 2 * pi * frequency # ω
    velocity = 3 * (10 ** 8) # v - speed of light
    wavelength = velocity / frequency # λ
    wave_number = 2 * pi / wavelength # k

    return amplitude * sin ((wave_number * distance) - (angular_velocity * time) + phase)

# signal 1
amplitude1: float = float(input("Enter the amplitude (V) of signal D1: "))
frequency1: float = float(input("Enter the frequency (Hz) of signal D1: "))
phase1: float = float(input("Enter the phase (rad) of signal D1: "))

# signal 2
amplitude2: float = float(input("Enter the amplitude (V) of signal D2: "))
frequency2: float = float(input("Enter the frequency (Hz) of signal D2: "))
phase2: float = float(input("Enter the phase (rad) of signal D2: "))

# fixed values
fixed_distance: float = float(input("Enter the fixed distance (x1): "))
fixed_time: float = float(input("Enter the fixed time (t1): "))

# domains
time_domain: ndarray = linspace(0, 1000, num=1000)
distance_domain: ndarray = linspace(0, 3*(10**8), num=1000)

# sum waves in time domain at fixed distance
wave1time: float64 = wave(amplitude1, frequency1, phase1, time_domain, fixed_distance)
wave2time: float64 = wave(amplitude2, frequency2, phase2, time_domain, fixed_distance)
sum_wave_time: float64 = wave1time + wave2time

# sum waves in distance domain at fixed time
wave1distance: float64 = wave(amplitude1, frequency1, phase1, fixed_time, distance_domain)
wave2distance: float64 = wave(amplitude2, frequency2, phase2, fixed_time, distance_domain)
sum_wave_distance: float64 = wave1distance + wave2distance

plt.figure(figsize=(12, 6))

# plot waves in time domain
plt.subplot(2, 1, 1)
plt.plot(time_domain, wave1time, label='D1')
plt.plot(time_domain, wave2time, label='D2')
plt.plot(time_domain, sum_wave_time, label='Sum')
plt.title(f'Signals in Time Domain at Fixed Distance x={fixed_distance}')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.legend()

#plot waves in distance domain
plt.subplot(2, 1, 2)
plt.plot(distance_domain, wave1distance, label='D1')
plt.plot(distance_domain, wave2distance, label='D2')
plt.plot(distance_domain, sum_wave_distance, label='Sum')
plt.title(f'Signals in Distance Domain at Fixed Time t={fixed_time}')
plt.xlabel('Distance (m)')
plt.ylabel('Amplitude (V)')
plt.legend()

plt.tight_layout()
plt.show()
