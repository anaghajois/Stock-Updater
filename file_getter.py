import urllib
from datetime import timedelta,date
import analyse_data

def get_excel_file():
    req_date = date.today() # - timedelta(2)
    if req_date.weekday()>=5:
        print "Weekend"
        return

    current_date = req_date.strftime('%Y-%m-%d')

    url_handle = urllib.URLopener()
    url = "http://www.fi.se/upload/50_Marknadsinfo/Blankning/Korta_positioner_"
    url += (current_date + '.xls')
    print url
    save_url = 'files/' + current_date +".xls"
    url_handle.retrieve(url, save_url)
    return save_url
