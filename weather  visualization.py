import requests
import matplotlib.pyplot as plt
import seaborn as sns

# <<< Replace with your real API key >>>
API_KEY = '958973a80d1c95ef974e302943712ebe'  

# List of cities
cities = ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Chennai']

# Dictionary to store temperature data
temperature_data = {}

# Loop through each city and get data
for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        temperature_data[city] = temp
        print(f"{city}: {temp}°C")
    else:
        print(f"Error fetching data for {city} - {response.status_code}")

# Plot the data using seaborn
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(x=list(temperature_data.keys()), y=list(temperature_data.values()), palette="coolwarm")

# Add chart labels
plt.title("Current Temperature in Indian Cities")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.tight_layout()

# Save the image and show it
plt.savefig("temperature_chart.png")
plt.show()
