import pandas as pd
import matplotlib.pyplot as plt

# Dati di traffico di rete (più realistici)
data = {
    "Device": [
        "PC", "Smartphone", "Server", "Laptop",
        "IoT Camera", "Printer", "Unknown_Device"
    ],
    "Packets_sent": [1200, 800, 3200, 1500, 400, 300, 5000],
    "Packets_received": [1100, 950, 2800, 1600, 420, 310, 1200]
}

df = pd.DataFrame(data)

print("Network traffic data:")
print(df)

# Grafico
df.plot(
    x="Device",
    y=["Packets_sent", "Packets_received"],
    kind="bar",
    figsize=(10,5)
)

plt.title("Network Traffic Analysis")
plt.ylabel("Number of Packets")
plt.xticks(rotation=45)
plt.show()

# Analisi differenza
df["Difference"] = df["Packets_sent"] - df["Packets_received"]

# Classificazione semplice
def classify_device(diff):
    if abs(diff) > 1000:
        return "HIGH RISK"
    elif abs(diff) > 300:
        return "MEDIUM RISK"
    else:
        return "NORMAL"

df["Risk_Level"] = df["Difference"].apply(classify_device)

print("\nTraffic analysis with risk classification:")
print(df[["Device", "Difference", "Risk_Level"]])
