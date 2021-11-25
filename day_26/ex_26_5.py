import pandas as pd


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

convert_dict = {'days': weather_c.keys(),
                'C_temp': weather_c.values()}


def cel_to_far(x:float) -> float:
    temp_f = (x * 9/5) + 32
    return(round(temp_f, 2))

weather = pd.DataFrame.from_dict(convert_dict, orient='columns')

weather['F_temp'] = weather['C_temp'].apply(lambda x: cel_to_far(int(x)))


print(weather.head(10))