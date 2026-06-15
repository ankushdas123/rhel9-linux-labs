# ' Servers =' '{ }'
Servers ={
    "Web_Server": 45,
    "Database Server": 85
}
print(Servers)
for name, usage in Servers.items():
    if usage > 80:
        print(f"Alert: {name} is at {usage}%! [Status: Danger]")
    else:
        print(f"Checking {name}: {usage}% [STATUS: SAFE]")

