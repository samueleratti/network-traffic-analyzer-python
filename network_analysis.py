import pandas as pd

# Dati fittizi di traffico di rete
data = {
    "Device": ["PC", "Smartphone", "Server", "Laptop"],
    "Packets_sent": [1200, 800, 3000, 1500],
    "Packets_received": [1100, 950, 2800, 1600]
}

# Creazione DataFrame
df = pd.DataFrame(data)

# Stampa dei dati
print("Network traffic data:")
print(df)

# Analisi semplice
print("\nTotal packets sent:", df["Packets_sent"].sum())
print("Total packets received:", df["Packets_received"].sum())
