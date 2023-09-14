# Sytulacja rzutu dwoma kośćmi.

from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die_1 = Die()
die_2 = Die(10)

results = [die_1.roll()+die_2.roll() for roll_num in range(50_000)]

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik', 'dtick': 1} # dtick : 1 -> nakazanie dodawania podpisu do każdego słupka
y_axis_config = {'title': 'Częstotliwośc występowania wartości'}
my_layout = Layout(title='Wynik rzucania kośćmi D6 i D10 pięćdziesiąt tysięcy razy',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout': my_layout}, filename='d6_d10.html')