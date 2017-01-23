import json
my_list=[1,2,3,4,5,6,7,8,9]
my_dict={'name':'ram'}
my_str='asm tech'
f=open('file123.txt','w')
json.dump(my_list,f)
json.dump(my_dict,f)
f.close()
