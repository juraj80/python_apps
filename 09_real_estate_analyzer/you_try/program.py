import os, csv

try:
    import statistics
except:
    import statistics_standin_for_py2 as statistics

from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('-------------------------------------------')
    print('    REAL ESTATE DATA MINING APP')
    print('-------------------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r') as fin:
        reader = csv.DictReader(fin)  # creates Ordered Dict
        purchases = []
        for row in reader:
            #           print(type(row), row)
            # print("Bed count: {}".format(row['beds']))
            p = Purchase.create_from_dict(row)  # creating Purchase object from dict
            #             p = Purchase(
            #                 lookup['street'],
            #                 lookup['city'],
            #                 lookup['zip'],
            #                 lookup['state'],
            #                 int(lookup['beds']),
            #                 int(lookup['baths']),
            #                 int(lookup['sq__ft']),
            #                 lookup['type'],
            #                 lookup['sale_date'],
            #                 float(lookup['price']),
            #                 float(lookup['latitude']),
            #                 float(lookup['longitude']))
            purchases.append(p)

        return purchases

        # header = fin.readline().strip()
        # print('found header: ' + header)
        #
        # reader = csv.reader(fin)
        #
        # for line in reader:
        #     print(line)


# def load_file_basic(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print('found header: ' + header)
#
#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')
#             bed_count = line_data[4]
#             lines.append(line_data)
#         print(lines[:5])

# def get_price(p):
#     return p.price


def query_data(data):  # data - list of purchase objects
    # most expensive house?
    data.sort(key=lambda p: p.price)
    #    data.sort(key=get_price)
    high_purchase = data[-1]
    print("The most expensive house is ${:,} with {} beds and {} baths.".format(high_purchase.price, high_purchase.beds,
                                                                                high_purchase.baths))

    # least expensive house
    low_purchase = data[0]
    print("The least expensive house is ${:,} with {} beds and {} baths.".format(low_purchase.price, low_purchase.beds,
                                                                                 low_purchase.baths))

    # average price house?
    # prices = []
    # for pur in data:
    #     prices.append(pur.price)
    prices = [p.price for p in data]  # list comprehension / to extract prices from dict to list

    avg_price = statistics.mean(prices)
    print("The average home price is ${:,}.".format(int(avg_price)))

    # average price of 2 bedroom house

    two_bed_homes = (p for p in data if announce(p, '2-bedroom, found {}'.format(p.beds)) and p.beds == 2)

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    avg_price = statistics.mean((announce(p.price, "price") for p in homes))
    avg_baths = statistics.mean((p.baths for p in homes))
    avg_sf = statistics.mean((p.sq__ft for p in homes))
    print("Average 2-bedroom home is ${:,}, baths={}, sq ft={:,}."
          .format(int(avg_price), round(avg_baths, 1), round(avg_sf, 1)))


def announce(item, msg):
    print("Pulling item {} for {}".format(item, msg))
    return item


if __name__ == '__main__':
    main()
