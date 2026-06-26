user_profile = {
    "name": "Ankush Das",
    "age": 25,
    "role": "Network Engineer",
    "skills": ["Python", "Networking", "Linux"]
}
print(user_profile["name"])  # Output: Ankush Das
user_profile["age"] = 26  # Update age  
user_profile["location"] = "Kolkata"  # Add new key-value pair  
print(user_profile)  # Output: {'name': 'Ankush Das', 'age': 26, 'role': 'Network Engineer', 'skills': ['Python', 'Networking', 'Linux'], 'location': 'Kolkata'}
server_config = {
    "ip": "192.168.1.1",
    "status": "Active"
}
server_config["status"] = "Down"
print(server_config)  # Output: {'ip': '192.168.1.1', 'status': 'Down'}
# Loop through dictionary items
for key, value in server_config.items():
    print(f"Key is {key} and Value is {value}")

