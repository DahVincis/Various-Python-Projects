# creating a dictionary based on 2 lists

whatever = ['vink', 'bing', 'tony', 'yas','tim']
another_list = ['ct','ny','ca','ak','nc']
live = {}
for x in range(len(whatever)):
    live[whatever[x]] = another_list[x]
print(live)