import pandas as pd
import click
import json


class Apps_n_Sites:
    def __init__(self, data_file):
        with open(data_file, 'r') as f:
            data = json.load(f)
        self.records = pd.DataFrame(data['installed_apps'])
        self.records["added_timestamp"] = pd.to_datetime(
            self.records['added_timestamp'], unit='s')
        self.records.set_index('added_timestamp', inplace=True)

    def get_year(self, year):
        return self.records[(self.records.index >= '{}-1-1'.format(year)) &
                            (self.records.index <= '{}-12-31'.format(year))]


@click.command()
@click.argument('data_file')
def main(data_file):
    apps = Apps_n_Sites(data_file)

    df_11 = apps.get_year(2012)
    print(df_11)


if __name__ == '__main__':
    main()
