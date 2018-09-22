import pandas as pd
import click
import json


@click.command()
@click.argument('data_file')
def main(data_file):
    with open(data_file, 'r') as f:
        data = json.load(f)
    print(data)
    df = pd.DataFrame(data['installed_apps'])
    df["added_timestamp"] = pd.to_datetime(df['added_timestamp'], unit='s')
    df.set_index('added_timestamp', inplace=True)

    df_11 = get_year(df, 2012)
    import pdb
    pdb.set_trace()


def get_year(df, year):
    return df[(df.index >= '{}-1-1'.format(year)) &
              (df.index <= '{}-12-31'.format(year))]


if __name__ == '__main__':
    main()
