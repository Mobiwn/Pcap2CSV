import sys
from pcap2csv.converter import PcapToCsvConverter

def main():
    if len(sys.argv) != 3:
        print("Usage: python convert_pcap.py <input_pcap_file> <output_csv_file>")
        sys.exit(1)

    pcap_file = sys.argv[1]
    csv_file = sys.argv[2]

    converter = PcapToCsvConverter(pcap_file, csv_file)
    converter.convert()

    print(f"Conversion complete: {csv_file}")

if __name__ == "__main__":
    main()
