tuple = ("a","b","c")
tuple_iterator = iter(tuple)
print(next(tuple_iterator))
print(next(tuple_iterator))
print(next(tuple_iterator))
#print(next(tuple_iterator))
#hata verir

for x in tuple:
    print(x)
#for loop iterator objesi yaratır
#her döngüde next() methodunu çalıştırır

list = ["1","2","3"]
list_iterator = iter(list)
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))
#print(next(list_iterator))
#hata verir

dict = {"key1": "a", "key2": "b", "key3": "c"}
dict_iterator = iter(dict)
print(next(dict_iterator))  
print(next(dict_iterator))
print(next(dict_iterator))
#print(next(dict_iterator))
#hata verir
#keys üzerinde iterasyon yapılır

set = {"a", "b", "c"}
set_iterator = iter(set)
print(next(set_iterator))
print(next(set_iterator))
print(next(set_iterator))
#print(next(set_iterator))
#hata verir

string = "hello world"
string_iterator = iter(string)
print(next(string_iterator))
print(next(string_iterator))
print(next(string_iterator))
print(next(string_iterator))
print(next(string_iterator))
print(next(string_iterator))
print(next(string_iterator))
print(next(string_iterator))
print(next(string_iterator))
print(next(string_iterator))
print(next(string_iterator))
#print(next(string_iterator))
#hata verir