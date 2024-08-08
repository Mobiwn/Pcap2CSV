import unittest
import os
import csv
from pcap2csv.converter import PcapToCsvConverter
from scapy.all import Ether, IP, TCP, UDP, wrpcap


class TestPcapToCsvConverter(unittest.TestCase):
    def setUp(self):
        """Set up a temporary pcap file for testing."""
        self.test_pcap = 'test.pcap'
        self.test_csv = 'test.csv'
        
        # Create a sample pcap file
        packets = [
            Ether()/IP(src="192.168.1.1", dst="192.168.1.2")/TCP(sport=12345, dport=80),
            Ether()/IP(src="192.168.1.2", dst="192.168.1.1")/UDP(sport=12345, dport=53),
        ]
        wrpcap(self.test_pcap, packets)
    
    def tearDown(self):
        """Clean up test files."""
        if os.path.exists(self.test_pcap):
            os.remove(self.test_pcap)
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)
    
    def test_conversion(self):
        """Test the conversion of pcap to CSV."""
        converter = PcapToCsvConverter(self.test_pcap, self.test_csv)
        converter.convert()
        
        self.assertTrue(os.path.exists(self.test_csv))
        
        with open(self.test_csv, mode='r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
        
        self.assertGreater(len(rows), 0)  # Ensure there's at least one row
        self.assertEqual(rows[0]['proto'], '6')  # Numeric value for TCP
        self.assertEqual(rows[1]['proto'], '17')  # Numeric value for UDP

if __name__ == '__main__':
    unittest.main()