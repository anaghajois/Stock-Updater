import os
import shutil
import file_getter
import analyse_data
import twitter_interface

dirs = ['files', 'charts']
for dir in dirs:
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)

file_url = file_getter.get_excel_file()
analyse_data.analyse_and_plot_graph(file_url)
twitter_interface.tweet_images_in_folder('charts/')
