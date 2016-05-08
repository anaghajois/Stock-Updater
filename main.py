import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime
import plot_graph

def transposed(lists):
   if not lists: return []
   return map(lambda *row: list(row), *lists)

def eq_date_range(start, end, intv):
    diff = (end  - start ) / intv
    for i in range(intv):
        yield (start + diff * i)
    yield end

def analyse_and_plot_graph(xls_file_name):
    df = pandas.read_excel('files/' + xls_file_name, 'Blankningar fi.se', index_col=None, na_values=['NA'],
                           header=6, skiprows=5)
    df.columns = ['pub_date', 'pos_holder', 'issuer', 'ISIN', 'percent', 'pos_date', 'comment']
    groups = df.groupby(df['issuer'].str.lower())

    count = 0
    for group in groups:
        file_name = group[1]['issuer'].values[0]
        holderGroups = group[1].groupby(by=['pos_holder'])
        uniqueHolders = list(set(group[1]['pos_holder'].values))

        dateStrs =  group[1]['pos_date'].values
        pos_dates = []
        percents = []
        for dateStr in dateStrs:
            print pandas.to_datetime(dateStr)
            pos_dates.append(pandas.to_datetime(dateStr))
        unique_dates = list(set(pos_dates))
        today = datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())
        unique_dates.append(today)
        unique_dates = sorted(unique_dates)
        unique_items= []

        for unique_date in unique_dates:
            item = (unique_date,[0] * len(uniqueHolders))
            unique_items.append(item)

        for holderGroup in holderGroups:
            try:
                holder_group_index =  uniqueHolders.index(holderGroup[0])
                print holderGroup[0],holder_group_index
                raw_percents = holderGroup[1]['percent'].values
                pos_dates_local = holderGroup[1]['pos_date'].values
                pos_dates_index = 0
                while pos_dates_index < len(pos_dates_local):
                    try:
                        item_index = unique_dates.index(pandas.to_datetime(pos_dates_local[pos_dates_index]))
                        print pandas.to_datetime(pos_dates_local[pos_dates_index]), str(raw_percents[pos_dates_index]).replace(',', '.')
                        unique_items[item_index][1][holder_group_index] = float(str(raw_percents[pos_dates_index]).replace(',', '.'))
                    except:
                        pass
                    pos_dates_index += 1

                    unique_item_index = 1
                    while unique_item_index < len(unique_items):
                        if unique_items[unique_item_index][1][holder_group_index] == 0:
                            unique_items[unique_item_index][1][holder_group_index] = unique_items[unique_item_index - 1][1][holder_group_index]
                        unique_item_index += 1
            except:
                pass

        #print the items
        for item in unique_items:
            print item


        newDF = pandas.DataFrame.from_items(unique_items, orient='index', columns = uniqueHolders)

        oldest_date = min(unique_dates)
        newest_date = max(unique_dates)

        date_intervals = list(eq_date_range(oldest_date, newest_date, 5))
        print 'date intervals:',date_intervals

        plot_graph.plot_area_graph(newDF, file_name, date_intervals)

        print '----'
        count += 1
