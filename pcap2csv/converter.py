import csv
from scapy.all import rdpcap, IP

class PcapToCsvConverter:
    def __init__(self, pcap_file, csv_file):
        self.pcap_file = pcap_file
        self.csv_file = csv_file

    def convert(self):
        packets = rdpcap(self.pcap_file)
        with open(self.csv_file, 'w', newline='') as csvfile:
            fieldnames = ['timestamp', 'src', 'dst', 'proto', 'length']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for pkt in packets:
                if IP in pkt:
                    writer.writerow({
                        'timestamp': pkt.time,
                        'src': pkt[IP].src,
                        'dst': pkt[IP].dst,
                        'proto': pkt[IP].proto,
                        'length': len(pkt)
                    })
                else:
                    # Handle non-IP packets or log them if needed
                    writer.writerow({
                        'timestamp': pkt.time,
                        'src': 'N/A',
                        'dst': 'N/A',
                        'proto': pkt[0].name,
                        'length': len(pkt)
                    })