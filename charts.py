# Nauka wizualizacji prostych danych

import matplotlib.pyplot as plt

plt.style.use('ggplot') # Bardzo ładne wizualnie wykresy :)

"""
input_values = list(range(1, 6))
print(input_values)
squares = [liczba*liczba for liczba in range(1,6)]

fig, ax = plt.subplots() # subplots -> pozwala wygenerować jeden lub więcej wykresów na tym samym rysunku.
# fig -> cały rysunek, czyli kolekcja wygenerowanych wykresów.
# ax -> przedstawia jeden wykres na rysunku.

ax.plot(input_values, squares, linewidth=3) # linewidth -> określa grubość linii na wykresie

# Zdefiniowanie tytułu wykresu i etykiet osi.
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

#Zdefiniowanie wielkości etykiet
ax.tick_params(axis='both', labelsize=14)

plt.show()
"""

x_values = range(1, 1001)
y_values = [x**2 for x in x_values] # smart!

fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c='pink', s=10) # scatter -> do wyświetlania poszczególnych punktów
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# punkty o większych wartościach Y mają kolor ciemnoniebieski, a o mniejszych jasnoniebieski.

# Zdefiniowanie tytułu wykresu i etykiet osi.
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

#Zdefiniowanie wielkości etykiet
ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 1100, 0, 1100000])

plt.show()