import tkinter as tk
from typing import Union


window = tk.Tk()
window.title('Mile to KM Converter')
window.minsize(height=120,
               width=160)
window.config(padx=30,
              pady=20)
user_input = tk.Entry(width=8)

miles_text = tk.Label(text='Miles')
is_equal_text = tk.Label(text='Is Equal to')
km_text = tk.Label(text='Km')


result = tk.Label(text='0')


def mile_to_km(mile:Union[int, float]=1) -> float:
    return(round(mile * 1.60934, 2))


def km_to_mile(km:Union[int, float]) -> float:
    return(round(km/1.60934, 2))


def converter_mi_to_km():
    miles = user_input.get()
    km = mile_to_km(int(miles))
    result.config(text=km)


button = tk.Button(text='Calculate',
                   command=converter_mi_to_km)


user_input.grid(column=1,
                row=0)

miles_text.grid(column=2,
                row=0)

is_equal_text.grid(column=0,
                   row=1)

result.grid(column=1,
            row=1)

km_text.grid(column=2,
             row=1)

button.grid(column=1,
            row=2)


tk.mainloop()