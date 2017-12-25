# import dependancies
import requests     # making calls to the api
import datetime     # date stamp for csv file
import sys


def make_api_call(timestamp, parse_date):
    timestamp += 43200
    rtn = ''
    currencies = [['Bitcoin', 'BTC'], ['Ethereum', 'ETH'], ['RIPPLE', 'XRP'],
                  ['Litecoin', 'LTC'], ['Dash', 'DASH'], ['Ethereum Classic', 'ETC'],
                  ['NEO', 'NEO'], ['EOS', 'EOS'], ['Lisk', 'LSK']]

    # make api call and save response
    for currency in currencies:
        url = 'https://min-api.cryptocompare.com/data/pricehistorical?fsym=' + currency[1]
        url += '&tsyms=CAD,USD,BTC,USD&ts='
        url += str(timestamp)
        response = requests.get(url)

        if response.status_code == 200:  # everthing went okay
            json_response = response.json()  # decode to JSON form
            cad_price = json_response[currency[1]]['CAD']
            usd_price = json_response[currency[1]]['USD']
            btc_price = json_response[currency[1]]['BTC']
            temp = str(parse_date.date()).split('-')
            temp = temp[2] + '-' + temp[1] + '-' + temp[0] + ', ' + currency[0] + ', ' + currency[1] + ', '
            temp += str(cad_price) + ', ' + str(usd_price) + ', ' + str(btc_price)

            timestamp -= 86400  # go back one day
            url = 'https://min-api.cryptocompare.com/data/pricehistorical?fsym='
            url += currency[1] + '&tsyms=CAD&ts=' + str(timestamp)
            previous_close_response = requests.get(url)
            if previous_close_response.status_code == 200:
                previous_close_json = previous_close_response.json()
                prev_close = previous_close_json[currency[1]]['CAD']
                delta_dollars = float(cad_price) - float(prev_close)
                delta_percentage = float(cad_price) / float(prev_close) - 1
                temp += ', {:.3f}, {:.5f}%\n'.format(delta_dollars, delta_percentage)

            rtn += temp

    return rtn


def main(dates):
    file_contents = []
    for date in dates:
        with open('tracker.csv', 'r') as f:
            file_contents = f.read().splitlines()
            lines = file_contents
            for i in range(1, len(lines), 9):
                temp_date = list(map(int, lines[i].split(',')[0].split('-')))
                temp_date = datetime.datetime(temp_date[2], temp_date[1], temp_date[0])
                parse_date = datetime.datetime(date[0], date[1], date[2])

                if temp_date == parse_date:
                    break
                elif temp_date >= parse_date:
                    # write values to this index
                    print('Currently fetching data for timestamp =', parse_date)
                    new_line = make_api_call(parse_date.timestamp(), parse_date)
                    new_line = new_line[:-1]
                    file_contents.insert(i, new_line)
                    with open('tracker.csv', 'w') as writeFile:
                        for contents in file_contents:
                            writeFile.write(contents + '\n')
                    break


if __name__ == '__main__':
    args = sys.argv
    args = args[1:]
    parsed_args = []
    for arg in args:
        arg = arg.split('-')
        parsed_args.append([int(arg[2]), int(arg[1]), int(arg[0])])
    main(parsed_args)
    print('FILE UPDATED SUCCESSFULLY')
