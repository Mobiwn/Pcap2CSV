import sys
import os

# Ensure the script can find the pcap2csv module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../pcap2csv')))

from converter import PcapToCsvConverter

def main():
    if len(sys.argv) != 3:
        print("Usage: python convert_pcap.py <pcap_file> <csv_file>")
        sys.exit(1)
    
    pcap_file, csv_file = sys.argv[1], sys.argv[2]
    
    converter = PcapToCsvConverter(pcap_file, csv_file)
    converter.convert()

if __name__ == "__main__":
    main()