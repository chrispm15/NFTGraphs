from opensea import OpenseaAPI
import matplotlib.pyplot as plt
from datetime import date


api = OpenseaAPI(apikey='YOUR API KEY GOES HERE')

collections = ['collectionA', 'collectionC', 'etc']

def graph(slugs):
    names = slugs
    datalist = []
    try:
        for slug in slugs:
            floor = api.collection_stats(collection_slug=slug)['stats']['floor_price']
            change1d = api.collection_stats(collection_slug=slug)['stats']['one_day_change']
            floor1d = floor / (1 + change1d)
            change7d = api.collection_stats(collection_slug=slug)['stats']['seven_day_change']
            floor7d = floor / (1 + change7d)
            change30d = api.collection_stats(collection_slug=slug)['stats']['thirty_day_change']
            floor30d = floor / (1 + change30d)

            created = api.collection(slug)['collection']['created_date']
            created = created.split(sep='T')[0]
            yymmdd = created.split(sep='-')
            time_ago = date.today() - date(int(yymmdd[0]), int(yymmdd[1]), int(yymmdd[2]))
            days_ago = str(time_ago).split()[0]
            if int(days_ago) <= 31:
                floor30d = floor
                floor7d = floor
                floor1d = floor


            data = [floor30d, floor7d, floor1d, floor]
            datalist.append(data)

        days = [30, 7, 1, 0]
        plt.rcParams["figure.figsize"] = [20.00, 8]
        plt.rcParams["figure.autolayout"] = True
        plt.style.use('dark_background')
        x = days

        for i in datalist:
            n = datalist.index(i)
            y = datalist[n]
            default_x_ticks = range(len(x))
            plt.plot(default_x_ticks, y, label = names[n])
            plt.xticks(default_x_ticks, x)
        plt.xlabel('Days Ago')
        plt.ylabel('Average Price (ETH)')
        plt.legend(loc="upper left")
        plt.show()
    except:
        print("There was an error in plotting these collections.\n\nMake sure the slugs are typed exactly as they appear in the collection's OpenSea URL.")
        quit()
