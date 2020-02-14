import numpy as np
import pickle
import json
import datetime
from pprint import pprint as pp

list_1 = np.load('201802120944013538.npy')

with open('201802120944012444_99.pkl', 'rb') as f:
    list_2 = pickle.load(f)

print(np.shape(list_1))
print(np.shape(list_2), type(list_2))
# #
# # def json_default(value):
# #     if isinstance(value, datetime.date):
# #         return value.strftime('%Y-%m-%d')
# #     raise TypeError('not JSON serializable')
# # #data = {'date': datetime.date.today()}
# # json_data = json.dumps(list_2, default=json_default)
# # print(json_data)
#
# print(json.dumps(list_2, indent=4))

#print(list_2)

print(list_2.keys())
pp(list_2)


f = open("dict.txt","w")
f.write( str(list_2) )
f.close()