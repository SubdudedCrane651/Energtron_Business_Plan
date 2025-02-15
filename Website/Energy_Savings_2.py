import matplotlib.pyplot as plt
from decimal import Decimal  # Import Decimal class
import argparse
import os

# Example data for highs and lows for each month in Quebec
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthsfr = ["jan", "fev", "mar", "avr", "mai", "jun", "jul", "août", "sep", "oct", "nov", "dec"]    
highs = [-6, -5, 1, 9, 17, 23, 25, 24, 19, 12, 4, -3]
lows = [-14, -13, -7, 1, 8, 13, 16, 15, 11, 5, -2, -9]

def calculate_savings(house_type, house_size, annual_expenditure, language='en'):
    # Calculate average temperature
    avg_temps = [(high + low) / 2 for high, low in zip(highs, lows)]
    # Convert annual_expenditure to float if it is of type Decimal
    if isinstance(annual_expenditure, Decimal):
        annual_expenditure = float(annual_expenditure)
    # Calculate monthly savings based on average temperature
    monthly_savings = [(annual_expenditure / 12) * (1 - avg_temp / 30) for avg_temp in avg_temps]
    return monthly_savings

def plot_savings(monthly_savings, language='en'):
    plt.figure(figsize=(10, 5))
    if language=='en':
        plt.plot(months, monthly_savings, marker='o', label='Monthly Savings')

        # Plotting high and low temperatures
        plt.plot(months, highs, marker='^', linestyle='--', label='Average Highs (°C)')
        plt.plot(months, lows, marker='v', linestyle='--', label='Average Lows (°C)')
        
    else:
        plt.plot(monthsfr, monthly_savings, marker='o', label='Sauver Mensuel')

        # Plotting high and low temperatures
        plt.plot(monthsfr, highs, marker='^', linestyle='--', label='Les Moyen Hauts (°C)')
        plt.plot(monthsfr, lows, marker='v', linestyle='--', label='Les Moyen Bas (°C)')
            

    if language == 'en':
        plt.title('Monthly Electrical Savings and Average Temperatures in Quebec')
        plt.xlabel('Month')
        plt.ylabel('Savings ($) / Temperature (°C)')
    elif language == 'fr':
        plt.title('Économies Électriques Mensuelles et Températures Moyennes au Québec')
        plt.xlabel('Mois')
        plt.ylabel('Économies ($) / Température (°C)')

    plt.legend()
    # Check if the file exists and delete it
    file_path=f"{path}quebec_savings_temperatures.png"
    print("File_path :"+file_path)
    if os.path.exists(file_path): 
        os.remove(file_path)
    plt.savefig(file_path)
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate and plot monthly electrical savings.')
    parser.add_argument('house_type', type=str, help='Type of house (e.g., Detached, Semi-Detached, etc.)')
    parser.add_argument('house_size', type=int, help='Size of the house in square feet')
    parser.add_argument('annual_expenditure', type=str, help='Annual electricity expenditure in dollars')
    parser.add_argument('--language', type=str, default='en', help='Language for the plot (en for English, fr for French)')
    parser.add_argument('path', type=str, help='Path to save')

    args = parser.parse_args()

    house_type = args.house_type
    house_size = args.house_size
    annual_expenditure = Decimal(args.annual_expenditure)
    path=args.path
    # if path=="\\":
    #     path=""
    if path=="Win":
         path="N:\\Visual Studio 2021\\Websites\\Energtron\\img\\"
    else:
        path="/var/www/Energtron/img/"
            
    language = args.language

    monthly_savings = calculate_savings(house_type, house_size, annual_expenditure, language)
    plot_savings(monthly_savings, language)
