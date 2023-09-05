import matplotlib.pyplot as plt

input_values = list(range(1, 6))
print(input_values)
squares = [liczba*liczba for liczba in range(1,6)]

plt.style.use('ggplot')
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