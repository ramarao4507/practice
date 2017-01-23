import json
my_list=[1,2,3,4,5,6,7,8,9]
my_dict={'name':'ram','otc':'asm','pack':['python','ajs','html']}
my_str='asm tech'
f=open('file123.txt','w')
print json.dumps(my_dict,indent=4)
json.dump(my_list,f)
json.dump(my_dict,f)
f.close()
