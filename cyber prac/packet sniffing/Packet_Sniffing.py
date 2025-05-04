from scapy.all import sniff

# Function to process and analyze each packet
def analyze_packet(packet):
    print(packet.summary())  # Print a one-line summary of the packet

    if packet.haslayer("IP"):
        ip_layer = packet["IP"]
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")

    if packet.haslayer("TCP"):
        tcp_layer = packet["TCP"]
        print(f"Source Port: {tcp_layer.sport}")
        print(f"Destination Port: {tcp_layer.dport}")

    print("-" * 50)

# Start sniffing packets (limit to 10 packets for demo)
sniff(prn=analyze_packet, count=10)
