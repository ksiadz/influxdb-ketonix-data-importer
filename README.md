# influxdb-ketonix-data-importer

Import your CSV ketones data from ketonix.com into your InfluxDB instance

# Installation and usage
```bash
git clone https://github.com/ksiadz/influxdb-ketonix-data-importer.git
cd influxdb-ketonix-data-importer
pip install -r requirements.txt
```

Download your ketonix.com results: [link](https://www.ketonix.com/index.php?option=com_ketonixstudy&task=12)

Copy the ketonix_username.csv file into an `influxdb-ketonix-data-importer` directory 
Run:
```bash
python import.py --ketonix_filename=your_ketonix_username.csv 
```

CLI options and help:
```bash
python import.py -h
```


