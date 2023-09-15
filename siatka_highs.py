import csv
from matplotlib import pyplot as plt
from datetime import datetime

# filename = 'data\\sitka_weather_2018_simple.csv'
filename = 'data\\death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) # Obiekt przeglądarki umieszczamy w zmiennej 'reader'.
    header_row = next(reader) # Funkcja next -> wartością zwrotną jest następny wiersz pochodzący z pliku.

    # Do odczytu które indeksy mają znaczące dla nas informacje
    for index, column_header in enumerate(header_row): # Enumerate -> pobiera indeksy i wartości poszczególnych elementów.
        print(index, column_header)

    # Pobieranie date oraz najwyższych i najniższych temperatur z pliku.
    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Brak danych dla {current_date}") # Obsługiwanie wyjątku.
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Wygenerowanie wykresu najniższych i najwyższych temperatur.
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10,5), dpi=128)
ax.plot(dates, highs, c='red') # linewidth -> określa grubość linii na wykresie
ax.plot(dates, lows, c='blue')
ax.fill_between(dates, highs, lows, facecolor ='blue', alpha=0.1) # Wypełniamy przestrzeń pomiędzy wykresami. Alpha określa przezroczystość koloru.

# Formatowanie wykresu.
ax.set_title("Najwyższa i najniższa temperatura dnia - 2018\nDolina Śmierci, Kalifornia", fontsize=16)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()