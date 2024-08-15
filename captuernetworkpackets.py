from scapy.all import sniff

# Define a callback function to process packets
def packet_callback(packet):
    print(packet.show())

# Capture packets
sniff(prn=packet_callback, count=10)  # Capture 10 packets
