from scapy.all import conf, RandIP, RandShort, wrpcap, IP, TCP, UDP, Ether
import random
import logging

# Suppress Scapy warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
conf.verb = 0  # Disable Scapy's verbosity

def generate_test_pcap(output_file, num_packets=1000):
    packets = []
    for _ in range(num_packets):
        src_ip = RandIP()
        dst_ip = RandIP()
        sport = RandShort()
        dport = RandShort()
        
        if random.choice([True, False]):
            packet = Ether() / IP(src=src_ip, dst=dst_ip) / TCP(sport=sport, dport=dport)
        else:
            packet = Ether() / IP(src=src_ip, dst=dst_ip) / UDP(sport=sport, dport=dport)

        packets.append(packet)
    
    wrpcap(output_file, packets)
    print(f"Generated {num_packets} packets in {output_file}")

if __name__ == "__main__":
    conf.checkIPaddr = False  # Disable MAC resolution
    generate_test_pcap("../tests/data/test.pcap", num_packets=5000)