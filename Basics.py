#!/usr/bin/env python
# coding: utf-8

# In[31]:


from csv import reader

### The Google Play data set ###
opened_file = open('googleplaystore.csv')
read_file = reader(opened_file)
android = list(read_file)
android_header = android[0]
android = android[1:]
print(android_header)
### The App Store data set ###
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
ios = list(read_file)
ios_header = ios[0]
ios = ios[1:]
print(ios_header)


# In[6]:


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line between rows
        
    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))

print(android_header)
print('\n')
explore_data(android, 0, 3, True)


# In[7]:


print(ios_header)
print('\n')
explore_data(ios, 0, 3, True)


# In[8]:


print(android[10472])  # incorrect row
print('\n')
print(android_header)  # header
print('\n')
print(android[0])      # correct row


# In[9]:


print(len(android))
del android[10472]  # don't run this more than once
print(len(android))


# In[10]:


for app in android:
    name = app[0]
    if name == 'Instagram':
        print(app)


# In[11]:


duplicate_apps = []
unique_apps = []

for app in android:
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)
    
print('Number of duplicate apps:', len(duplicate_apps))
print('\n')
print('Examples of duplicate apps:', duplicate_apps[:15])


# In[12]:


reviews_max = {}

for app in android:
    name = app[0]
    n_reviews = float(app[3])
    
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
        
    elif name not in reviews_max:
        reviews_max[name] = n_reviews


# In[13]:


print('Expected length:', len(android) - 1181)
print('Actual length:', len(reviews_max))


# In[14]:


android_clean = []
already_added = []

for app in android:
    name = app[0]
    n_reviews = float(app[3])
    
    if (reviews_max[name] == n_reviews) and (name not in already_added):
        android_clean.append(app)
        already_added.append(name) # make sure this is inside the if block


# In[15]:


explore_data(android_clean, 0, 3, True)


# In[16]:


print(ios[813][1])
print(ios[6731][1])

print(android_clean[4412][0])
print(android_clean[7940][0])


# In[17]:


def is_english(string):
    
    for character in string:
        if ord(character) > 127:
            return False
    
    return True

print(is_english('Instagram'))
print(is_english('爱奇艺PPS -《欢乐颂2》电视剧热播'))


# In[18]:


print(is_english('Docs To Go™ Free Office Suite'))
print(is_english('Instachat 😜'))

print(ord('™'))
print(ord('😜'))


# In[19]:


def is_english(string):
    non_ascii = 0
    
    for character in string:
        if ord(character) > 127:
            non_ascii += 1
    
    if non_ascii > 3:
        return False
    else:
        return True

print(is_english('Docs To Go™ Free Office Suite'))
print(is_english('Instachat 😜'))
print(is_english('爱奇艺PPS -《欢乐颂2》电视剧热播'))


# In[20]:


android_english = []
ios_english = []

for app in android_clean:
    name = app[0]
    if is_english(name):
        android_english.append(app)
        
for app in ios:
    name = app[1]
    if is_english(name):
        ios_english.append(app)
        
explore_data(android_english, 0, 3, True)
print('\n')
explore_data(ios_english, 0, 3, True)


# In[21]:


android_final =[]
ios_final = []

for app in android_english:
    price = app[7]
    if price == '0' :
        android_final.append(app)

for app in ios_english:
    price = app[4]
    if price == '0.0' :
        ios_final.append(app)
        
        
print(len(android_final))
print(len(ios_final))


# In[22]:


#start analysing by determining the most common genres for each market
def freq_table(dataset, index):
    table = {}
    total = 0
    for row in dataset :
        total +=1
        value = row[index]
        if value in table:
            table[value] +=1
        else: table[value] =1
            
    table_percentage = {}
    for key in table :
        percentage = (table[key] / total) * 100
        table_percentage[key] = percentage
        
    return table_percentage

def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table :
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)
    table_sorted = sorted(table_display , reverse=True)
    for entry in table_sorted :
        print(entry[1], ':', entry[0])
            

android_category = display_table(android_final, 1)
print('\n')
android_genre = display_table(android_final, -4)
print('\n')
ios_genres = display_table(ios_final, -5)


# In[37]:


#most popular apps on AppStore
freq_genres = freq_table(ios_final, -5)
#print(ios_genres)

for genre in freq_genres:
    total = 0
    #total : the sum of user ratings
    len_genre = 0
    #len: number of apps specific to each genre
    for app in ios_final :
        genre_app = app[-5]
        if genre_app == genre :
            user_rating = float(app[5])
            total += user_rating
            len_genre += 1
    avg_user_rating = total/len_genre
    print(genre,':', avg_user_rating)
    


# In[39]:





# In[35]:


freq_category = freq_table(android_final, 1)
#print(freq_category)
for category in freq_category :
    total = 0
    #total : sum of instal to each genre
    len_category = 0
    #number of apps to each genre
    for app in android_final :
        category_app = app[1]
        if category_app == category :
            install_num = app[5]
            install_num = install_num.replace('+', '')
            install_num = install_num.replace(',' , '')
            install_num = float(install_num)
            total += install_num
            len_category += 1
    avg_install_num = total / len_category
    print(category, ':', avg_install_num)


# In[40]:


for app in android_final:
    if app[1]=='ART_AND_DESIGN':
        print(app[0], ':', app[5])


# In[ ]:




