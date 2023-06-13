from csv import reader

with open('twitter.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)
    #print(list_of_rows)

N=1
def specified_element(nums, N):
    result = [i[N] for i in nums]
    return result
splitted_arr = (specified_element(list_of_rows, N))

my_dict = {}
for sublist in splitted_arr:
        if sublist not in my_dict:
            my_dict[sublist] = 0
        my_dict[sublist] += 1
#print (my_dict)

dict_sortedd= dict(sorted(my_dict.items(), key=lambda item: item[1])) #sorted by value
#print (dict_sortedd)

print ("Enter number of top influencer's place")
x = int(input())
idd = list(dict_sortedd.items())[-x][0]
followers = list(dict_sortedd.items())[-x][1]
print("The", x, "st TOP INFLUENCER is ID", idd, "with number of follwers =", followers)