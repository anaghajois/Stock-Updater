import urllib
from datetime import timedelta,date
import analyse_data

def get_excel_file():
    url_handle = urllib.URLopener()
    url = "http://www.fi.se/upload/50_Marknadsinfo/Blankning/Korta_positioner_"
    if date.today().weekday()>=5:
        print "Weekend"
        return
    date = date.today() - timedelta(1)
    current_date = date.strftime('%Y-%m-%d')
    url += (current_date + '.xls')
    print url
    save_url = 'files/' + current_date +".xls"
    url_handle.retrieve(url, save_url)
    return save_url
