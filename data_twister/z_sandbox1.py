import log
import conf
import view_csv
import data_profiler

#print(conf.LogFolder)

#('oscar_age_female.csv',r'C:\Users\ilkay_senturk\git\home\data_twister\data')

data_profiler.profile_csv_view('ecommerce_data.csv',r'C:\Users\ilkay_senturk\git\home\data_twister\data')
#out=csv_file.read_csv()

#print(out)
#out2=csv_file.file_size_csv()

#out3=csv_file.sample_data(6,head=False)
#csv_file.test()
