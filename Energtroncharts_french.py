# pythoncode.py
# importing the required module
import xlwings as xw
import matplotlib.pyplot as plt 

#graph function which is to be called from python code(Calling function in VBA Editior)
def graph():
        # Open the workbook and get the active sheet
        wb = xw.Book("C:\\Users\\rchrd\\Documents\\Richard\\Plan d'affaires Energtron.xlsm")
        sht = wb.sheets['Sheet1']

        # x axis values (Expense descriptions)
        Expense = [str(exp) for exp in sht.range('A4:A27').value]

        # corresponding y axis values (Total cost)
        total_cost = [float(cost) for cost in sht.range('E4:E27').value]

        # Assign darker colors for each bar
        colors = ['#e6194b', '#3cb44b', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#008080', '#800000', '#808000', '#000075', '#000000']

        # Ensure we have enough colors by repeating the color list if necessary
        colors = (colors * ((len(total_cost) // len(colors)) + 1))[:len(total_cost)]

        # Create a bar plot
        fig, ax = plt.subplots()
        bars = plt.bar(range(len(Expense)), total_cost, color=colors)

        # Add the expense descriptions below the bars with black text
        for bar, exp in zip(bars, Expense):
            plt.text(bar.get_x() + bar.get_width()/2, -2, exp, ha='center', va='top', fontsize='x-small', color='black', rotation=90)

        # Adjust the limits, ticks, and increments
        ax.set_ylim(0, max(total_cost) * 1.1)
        ax.set_yticks(range(0, int(max(total_cost) * 1.1) + 1, 10000))
        ax.set_xticks(range(len(Expense)))
        ax.set_xticklabels([])  # Hide the default x-tick labels

        # naming the y axis
        plt.ylabel('MONTANT')

        # giving a title to the report
        plt.title('EXPENDITURES PAR COUTS ITEMS')

        # Adjust the bottom margin to fit the text
        plt.subplots_adjust(bottom=0.5)

        # Save the plot to a file
        plot_path = 'C:\\Users\\rchrd\\Documents\\Richard\\plot2.png'
        plt.savefig(plot_path)

        # function to show the plot (optional, if you want to display it separately)
        plt.show()

        # Insert the plot as a picture in Excel starting from cell G1
        sht.pictures.add(plot_path, name='MyBarGraph', update=True, left=sht.range('G1').left, top=sht.range('G1').top)

        print("Bar graph created and added to the Excel sheet.")



def linegraph():
    # Open the workbook and get the active sheet
    wb = xw.Book("C:\\Users\\rchrd\\Documents\\Richard\\Plan d'affaires Energtron.xlsm")
    sht = wb.sheets['Sheet1']

    # Months of the year for x-axis
    months = ['jan', 'fév', 'mar', 'avr', 'mai', 'jun', 'jul', 'août', 'sep', 'oct', 'nov', 'dec']

    # Expenses descriptions (each row from F43 to F55)
    expenses = [str(exp) for exp in sht.range('F43:F55').value]

    # Amounts for each month (columns G to R for each expense row)
    amounts = [sht.range(f'G{row}:R{row}').value for row in range(43, 56)]

    # Assign different colors for each line
    colors = ['#e6194b', '#3cb44b', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#800000', '#808000']

    # Ensure we have enough colors by repeating the color list if necessary
    colors = (colors * ((len(expenses) // len(colors)) + 1))[:len(expenses)]

    # Create a line plot
    fig, ax = plt.subplots()

    # Plot each expense with its unique color
    for idx, (exp, amounts_row, color) in enumerate(zip(expenses, amounts, colors)):
        ax.plot(months, amounts_row, marker='o', linestyle='-', color=color, label=exp)

    # Add labels and title
    plt.xlabel('Mois')
    plt.ylabel('Montant')
    plt.title('Expenditures Mensuels')

    # Add legend at the bottom
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3, fontsize='small')

    # Save the plot to a file
    plot_path = 'C:\\Users\\rchrd\\Documents\\Richard\\line_plot_expenses.png'
    plt.savefig(plot_path, bbox_inches='tight')

    # function to show the plot (optional, if you want to display it separately)
    plt.show()

    # Insert the plot as a picture in Excel starting from cell F62
    sht.pictures.add(plot_path, name='MyLineGraph', update=True, left=sht.range('F62').left, top=sht.range('F62').top)

    print("Line graph created and added to the Excel sheet.")

def linegraph2():
    # Open the workbook and get the active sheet
    wb = xw.Book("C:\\Users\\rchrd\\Documents\\Richard\\Plan d'affaires Energtron.xlsm")
    sht = wb.sheets['Sheet1']

    # Months of the year for x-axis
    months = ['jan', 'fév', 'mar', 'avr', 'mai', 'jun', 'jul', 'août', 'sep', 'oct', 'nov', 'dec']

    # Revenue descriptions (each row from F34 to F37)
    revenues = [str(rev) for rev in sht.range('F34:F37').value]

    # Amounts for each month (columns G to R for each revenue row)
    revenue_amounts = [sht.range(f'G{row}:R{row}').value for row in range(34, 38)]

    # Assign different colors for each line
    colors = ['#e6194b', '#3cb44b', '#4363d8', '#f58231']

    # Ensure we have enough colors by repeating the color list if necessary
    colors = (colors * ((len(revenues) // len(colors)) + 1))[:len(revenues)]

    # Create a line plot
    fig, ax = plt.subplots()

    # Plot each revenue with its unique color
    for rev, amounts_row, color in zip(revenues, revenue_amounts, colors):
        ax.plot(months, amounts_row, marker='o', linestyle='-', color=color, label=rev)

    # Add labels and title
    plt.xlabel('Mois')
    plt.ylabel('Montant')
    plt.title('Revenue Mensuels')

    # Add legend at the bottom
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, fontsize='small')

    # Save the plot to a file
    plot_path = 'C:\\Users\\rchrd\\Documents\\Richard\\line_plot_revenue.png'
    plt.savefig(plot_path, bbox_inches='tight')

    # function to show the plot (optional, if you want to display it separately)
    plt.show()

    # Insert the plot as a picture in Excel starting from cell G91
    sht.pictures.add(plot_path, name='MyLineGraphRevenue', update=True, left=sht.range('G91').left, top=sht.range('G91').top)

    print("Line graph for Monthly Revenue created and added to the Excel sheet.")


def hello_excel():
    #    wb = xw.Book.caller()
    wb = xw.Book('C:\\Users\\rchrd\\Documents\\Richard\\Espacejeux_Data.xlsm')
#     sht = xw.sheets.active
#     sheet = wb.sheets[0]
    sheet = wb.sheets['Sheet1']

    sheet['A2'].value = 'Hello, Excel!'

#graph()
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        globals()[sys.argv[1]]()
