from SQLWorking import *

date = "10/04/2022"
game = fetch_values_from_time_table(date)

for value in game:
    print(value)