import os
# Path to collect data from the Resources folder
output_data = os.path.join("resources", "output.txt")

# Open the file on the declared path
with open(output_data, 'w') as txtfile:

    # Write the first row (column headers)
    txtfile.write('Total Votes: 369711\n')

    # Write the second row
    txtfile.write('Diana DeGette: 73.812% (272892)\n')

    # Write the third row
    txtfile.write('Charles Casper Stockham: 23.049% (85213)\n')

    # Write the fourth row
    txtfile.write('Raymon Anthony Doane: 3.139% (11606)\n')

    # Write the fifth row
    txtfile.write('Winner: Diana DeGette\n')
print(f"Output saved to {output_data}")
