import mysql.connector
import matplotlib.pyplot as plt
from decimal import Decimal  # Import Decimal class

# Example data for highs and lows for each month in Quebec
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
highs = [-6, -5, 1, 9, 17, 23, 25, 24, 19, 12, 4, -3]
lows = [-14, -13, -7, 1, 8, 13, 16, 15, 11, 5, -2, -9]

def calculate_savings(house_type, house_size, annual_expenditure):
    # Calculate average temperature
    avg_temps = [(high + low) / 2 for high, low in zip(highs, lows)]
    # Convert annual_expenditure to float if it is of type Decimal
    if isinstance(annual_expenditure, Decimal):
        annual_expenditure = float(annual_expenditure)
    # Calculate monthly savings based on average temperature
    monthly_savings = [(annual_expenditure / 12) * (1 - avg_temp / 30) for avg_temp in avg_temps]
    return monthly_savings

db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'sys'
}

cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()

query = "SELECT house_type, square_feet, yearlycost FROM en_houseinfo"
cursor.execute(query)

data = cursor.fetchall()
cursor.close()
cnx.close()

savings_data = []

for row in data:
    house_type, square_feet, yearlycost = row
    monthly_savings = calculate_savings(house_type, square_feet, yearlycost)
    savings_data.append(monthly_savings)

plt.figure(figsize=(10, 5))
for idx, savings in enumerate(savings_data):
    plt.plot(months, savings, marker='o', label=f'House {idx+1} Savings')

# Plotting high and low temperatures
plt.plot(months, highs, marker='^', linestyle='--', label='Average Highs (°C)')
plt.plot(months, lows, marker='v', linestyle='--', label='Average Lows (°C)')

plt.title('Monthly Electrical Savings and Average Temperatures in Quebec')
plt.xlabel('Month')
plt.ylabel('Savings ($) / Temperature (°C)')
plt.legend()
plt.savefig('quebec_savings_temperatures.png')
plt.show()
