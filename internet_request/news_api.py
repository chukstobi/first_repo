import requests
import datetime

response = requests.get("http://checklight.pythonanywhere.com/streets")
data = response.json()
streets_list = data["streets"]

# one = data["streets"][13]
# history = data["streets"][13]["history"]
# time = history['time_line']

# time_status = ""
# for time_status in time:
#     if time_status['status'] == 0:
#         print(time_status['time'], "OFF")
#     elif time_status['status'] == 1:
#         print(time_status['time'], "ON")
        
       




# for streets in streets_list:
#     print(one)
#     print(streets["name"].ljust(27), '|', streets["state"].ljust(5),'|', streets["status"],"|", streets["avg_power"])

data_found = []
for index, street in enumerate(streets_list):
    # name, lga, state, avg_power = line.split(",")
    data_found.append({
        "name":street["name"],
        "lga":street["lga"],
        "state":street["state"],
        "avg_power":street["avg_power"]
    })
    print()
    print(index, street["name"])
selected_option = int(input("Above are the streets pick one \n> "))

print("\n###########################")
print(data_found[selected_option]["name"].upper())
print("###########################\n")
print(data_found[selected_option]["lga"],data_found[selected_option]["state"])
print("\n###########################")
print("###########################\n")