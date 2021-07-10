# influxdb-ketonix-data-importer

Import your csv ketones data from ketonix.com into your InfluxDB instance

```bash
pip install -r requirements.txt
```

Copy the ketonix_username.csv file into a directory
Run:
```bash
python import.py --ketonix_filename=your_ketonix_username.csv 
```

CLI flags and help:
```bash
python import.py -h
```

