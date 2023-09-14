# Symulacja rzutu jedną kością.

from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Utworzenie kości typu D6.
die = Die()

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analiza wyników.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Wizualizacja wyników.
x_values = list(range(1, die.num_sides+1)) # Lista rozpoczynająca się od 1 i kończąca na ilości ścianek kości.
data = [Bar(x=x_values, y=frequencies)] # Przedstawia zbiór danych jako wykres słupkowy.

x_axis_config = {'title': 'Wynik'} # Opcje konfiguracyjne przechowywane w postaci słownika.
y_axis_config = {'title': 'Częstotliwośc występowania wartości'}
my_layout = Layout(title='Wynik rzucania pojedynczą kością D6 tysiąc razy',
                   xaxis=x_axis_config, yaxis=y_axis_config) # Klasa Layout zwraca obiekt określający wygląd i konfigurację wykresu.
offline.plot({'data':data, 'layout': my_layout}, filename='d6.html')