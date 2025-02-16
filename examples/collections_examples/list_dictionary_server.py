# Initialiseren van de dictionary
server_info = {
    "ip": "10.0.0.1",
    "os": "Linux",
    "services": ["HTTP", "SSH", "FTP"]
}

# Toegang tot waarden in de dictionary
print(f"Server IP: {server_info['ip']}")  # Output: Server IP: 10.0.0.1
print(f"Besturingssysteem: {server_info['os']}")  # Output: Besturingssysteem: Linux
print(f"Draaiende services: {', '.join(server_info['services'])}")  # Output: Draaiende services: HTTP, SSH, FTP

# Een nieuw item toevoegen
server_info["uptime"] = "24 dagen"
print(f"Server uptime: {server_info['uptime']}")  # Output: Server uptime: 24 dagen

# Een bestaande waarde wijzigen
server_info["ip"] = "192.168.1.1"
print(f"Nieuw IP-adres: {server_info['ip']}")  # Output: Nieuw IP-adres: 192.168.1.1

# Een service toevoegen aan de lijst van services
server_info["services"].append("DNS")
print(f"Bijgewerkte services: {', '.join(server_info['services'])}")  # Output: Bijgewerkte services: HTTP, SSH, FTP, DNS

# Toegang tot zowel de sleutels als waarden (items) in de dictionary
print("\nVolledige serverinformatie:")
for key, value in server_info.items():
    print(f"{key}: {value}")


# Toegang tot alleen de sleutels (keys) in de dictionary
print ("\nSleutels in de dictionary:")
keys = server_info.keys()
print(f"Sleutels in de dictionary: {', '.join(keys)}")  
# Output: Sleutels in de dictionary: ip, os, services, uptime

# Toegang tot alleen de waarden (values) in de dictionary
print ("\nWaarden in de dictionary:")
values = server_info.values()
print(f"Waarden in de dictionary: {', '.join(map(str, values))}")  
# Output: Waarden in de dictionary: 192.168.1.1, Linux, ['HTTP', 'SSH', 'FTP', 'DNS'], 24 dagen



#Here’s an example using the server_info dictionary for a similar concept: counting occurrences based on certain conditions. Instead of logs, we will process the services in the server_info data and count how often each service appears in a new list of entries.
print ("\nVoorbeeld van het tellen van het aantal services:")
# Example server information
server_info = {
    "ip": "192.168.1.1",
    "os": "Linux",
    "services": ["HTTP", "SSH", "FTP", "HTTP", "DNS", "SSH", "FTP", "HTTP"]
}

# Dictionary om het aantal keer dat elke service voorkomt bij te houden
service_counts = {}

# Loop door de services en tel het aantal keer dat elke service voorkomt
for service in server_info["services"]:
    # Werk de dictionary bij met het aantal keer dat de service voorkomt
    # ,0 is een standaardwaarde als de sleutel niet wordt gevonden
    service_counts[service] = service_counts.get(service, 0) + 1
    # print (service_counts.get(service, 0))  # Debug-uitvoer (optioneel)

# Geef de resultaten weer
print("Aantal services:")
for service, count in service_counts.items():
    print(f"{service}: {count}")

