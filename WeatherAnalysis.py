import re

def read_temperature_data(filename):
    with open(filename, 'r') as file:
        data = file.read()
    # Use regex to extract dates and temperatures
    pattern = r'(\d{4}-\d{2}-\d{2}),(-?\d+)°C'
    matches = re.findall(pattern, data)
    return [(match[0], int(match[1])) for match in matches]

def calculate_yearly_averages(files):
    yearly_data = {}
    for filename in files:
        data = read_temperature_data(filename)
        for date, temp in data:
            year = date.split('-')[0]
            if year not in yearly_data:
                yearly_data[year] = []
            yearly_data[year].append(temp)
    
    yearly_averages = {}
    for year, temps in yearly_data.items():
        yearly_averages[year] = sum(temps) / len(temps)
    
    return yearly_averages

def find_year_with_highest_average(yearly_averages):
    return max(yearly_averages, key=yearly_averages.get)

def main():
    # List of weather data files
    files = ['weather_data/weather_2020.txt', 'weather_data/weather_2021.txt']  # Add more files as needed
    
    yearly_averages = calculate_yearly_averages(files)
    
    for year, avg_temp in yearly_averages.items():
        print(f"Average temperature for {year}: {avg_temp:.2f}°C")
    
    highest_year = find_year_with_highest_average(yearly_averages)
    print(f"Year with the highest average temperature: {highest_year} with {yearly_averages[highest_year]:.2f}°C")

if __name__ == "__main__":
    main()
