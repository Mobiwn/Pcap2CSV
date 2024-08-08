from scapy.all import IP, TCP, UDP, Ether, wrpcap
from scapy.utils import RandIP, RandShort
import random

def generate_test_pcap(output_file, num_packets=1000):
    packets = []
    for _ in range(num_packets):
        src_ip = RandIP()
        dst_ip = RandIP()
        sport = RandShort()
        dport = RandShort()
        
        # Randomly choose between TCP and UDP packets
        if random.choice([True, False]):
            packet = Ether() / IP(src=src_ip, dst=dst_ip) / TCP(sport=sport, dport=dport)
        else:
            packet = Ether() / IP(src=src_ip, dst=dst_ip) / UDP(sport=sport, dport=dport)

        packets.append(packet)
    
    # Write the packets to a pcap file
    wrpcap(output_file, packets)
    print(f"Generated {num_packets} packets in {output_file}")

if __name__ == "__main__":
    generate_test_pcap("../tests/data/test.pcap", num_packets=5000)