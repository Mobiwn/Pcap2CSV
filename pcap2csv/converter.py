import csv
from scapy.all import rdpcap

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
                writer.writerow({
                    'timestamp': pkt.time,
                    'src': pkt[0][1].src if len(pkt) > 1 else 'N/A',
                    'dst': pkt[0][1].dst if len(pkt) > 1 else 'N/A',
                    'proto': pkt[0].name,
                    'length': len(pkt)
                })
