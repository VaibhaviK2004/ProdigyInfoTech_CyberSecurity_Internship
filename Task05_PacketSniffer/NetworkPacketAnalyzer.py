from scapy.all import sniff, IP, TCP, UDP, ICMP

def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src = ip_layer.src
        dst = ip_layer.dst
        proto = ip_layer.proto

        print(f"\n[+] Packet Captured")
        print(f"Source IP: {src}")
        print(f"Destination IP: {dst}")
        
        if packet.haslayer(TCP):
            print("Protocol: TCP")
            print(f"Payload: {bytes(packet[TCP].payload)}")
        elif packet.haslayer(UDP):
            print("Protocol: UDP")
            print(f"Payload: {bytes(packet[UDP].payload)}")
        elif packet.haslayer(ICMP):
            print("Protocol: ICMP")
        else:
            print("Protocol: Other")

print("[*] Starting Packet Sniffer... Press Ctrl+C to stop.")
sniff(prn=process_packet, store=False)
