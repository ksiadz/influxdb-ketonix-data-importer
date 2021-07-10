from influxdb import InfluxDBClient
import fire
from csv import reader

def main(ketonix_filename='ketonix_username.csv', influx_host='localhost', influx_port=8086, inlux_user='root', influx_password='root', influx_dbname='health'):
    """Parse a ketonix.com csv ketones measureents results into a InfluxDB."""
    influx_user = 'root'
    influx_password = 'root'
    influx_dbname = 'health'

    client = InfluxDBClient(influx_host, influx_port, influx_user, influx_password, influx_dbname)

    with open(ketonix_filename, 'r') as read_obj:
        csv_reader = reader(read_obj, delimiter=';')
        measurement_date=""
        measurement=0
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            measurement_date=row[0]+"T"+row[1]+"Z"
            measurement_name=row[2]
            measurement=row[3]

            json_body = [
                {
                    "measurement": "Ketonix_" + measurement_name,
                    "time": measurement_date,
                    "fields": {
                        "Float_value": float(measurement),
                        "String_value": measurement_name,
                        "Bool_value": True
                    }
                }
            ]

            print("Write points: {0}".format(json_body))
            client.write_points(json_body)

if __name__ == '__main__':
  fire.Fire(main)
