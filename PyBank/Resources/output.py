import os
# Path to collect data from the Resources folder
output_data = os.path.join("resources", "output.txt")

# Open the file on the declared path
with open(output_data, 'w') as txtfile:

    # Write the first row (column headers)
    txtfile.write('Total Months: 86\n')

    # Write the second row
    txtfile.write('Total: $22564198\n')

    # Write the third row
    txtfile.write('Average Change: $-8311.11\n')

    # Write the fourth row
    txtfile.write('Greatest Increase in Profits: Jul-16 ($1862002)\n')

    # Write the fifth row
    txtfile.write('Greatest Decrease in Profits: Jan-14 ($-1825558)\n')
print(f"Output saved to {output_data}")