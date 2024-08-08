# Pcap2CSV

`Pcap2CSV` is a Python utility for converting packet capture (PCAP) files into CSV format. This tool allows for easy analysis of network traffic by converting detailed packet data into a structured CSV file, which can be used for further analysis or reporting. 📊

## Features

- 🗂️ Convert PCAP files to CSV format
- 🌐 Support for IP, TCP, UDP, and other protocols
- 🖥️ Simple command-line interface
- 🧪 Includes utility scripts for generating test PCAP files
- ✅ Unit tests to ensure code reliability

## Installation

1. **Clone the Repository** 🚀

    ```bash
    git clone https://github.com/mobiwn/Pcap2CSV.git
    cd Pcap2CSV
    ```

2. **Set Up a Virtual Environment** 🏗️

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies** 📦

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Converting a PCAP File to CSV

To convert a PCAP file to CSV, use the `convert_pcap.py` script:

```bash
python scripts/convert_pcap.py <pcap_file> <csv_file>
```

**Example:**

```bash
python scripts/convert_pcap.py tests/data/test.pcap tests/data/test.csv
```

### Generating a Test PCAP File

To generate a test PCAP file with random packets, use the `generate_test_pcap.py` script:

```bash
python scripts/generate_test_pcap.py
```

This will generate a `test.pcap` file in the `tests/data/` directory.

## Project Structure

Here is the structure of the `Pcap2CSV` project as visible in GitHub:

```
Pcap2CSV/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── pcap2csv/
│   ├── __init__.py
│   └── converter.py
├── scripts/
│   ├── convert_pcap.py
│   └── generate_test_pcap.py
└── tests/
    ├── __init__.py
    └── data/
```

## Running Tests

To run the unit tests, use the following command:

```bash
python -m unittest discover -s tests
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to propose changes or improvements. 🤝

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 📜

## Contact

For any questions or support, please contact [mobin.kh15@gmail.com](mobin.kh15@gmail.com). 📧
