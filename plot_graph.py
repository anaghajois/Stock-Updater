import matplotlib.pyplot as plt

def plot_area_graph(dF, file_name, date_intervals):
    ax = dF.plot.area(title=file_name, xticks= date_intervals);
    ax.xaxis.set_major_formatter(date_intervals.DateFormatter('%b%d'))
    lgd = plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    fig = ax.get_figure()
    fig.set_size_inches(12.5, 6.5)
    fig.subplots_adjust(left = 0.1, right=0.6)
    fig.savefig('charts/' + file_name +'.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
