from scapy.all import IP, ICMP, send
import time

# Fake source IP (spoofed)
fake_source_ip = "192.168.1.100"  # Replace with any spoofed IP

# Target IP (destination)
target_ip = "192.168.1.101"       # Replace with the actual test target

# Create the spoofed packet
packet = IP(src=fake_source_ip, dst=target_ip) / ICMP()

# Send the packet 5 times and print status
sent_count = 0
for i in range(5):
    print(f"Sending packet {i + 1} to {target_ip} from {fake_source_ip}")
    send(packet)  # Send the packet
    sent_count += 1  # Increment sent packet counter
    time.sleep(1)  # 1-second delay between each send

print(f"\nSent {sent_count} packets.")  # Final confirmation of packet sending
