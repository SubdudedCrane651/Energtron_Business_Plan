import matplotlib.pyplot as plt

# Example data for highs and lows for each month in Quebec
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
highs = [-6, -5, 1, 9, 17, 23, 25, 24, 19, 12, 4, -3]
lows = [-14, -13, -7, 1, 8, 13, 16, 15, 11, 5, -2, -9]

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(months, highs, marker='o', label='Highs')
plt.plot(months, lows, marker='o', label='Lows')
plt.title('Average High and Low Temperatures in Quebec')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.legend()

# Save the plot as a PNG file
plt.savefig('quebec_temperatures.png')

# Show the plot (optional)
plt.show()
