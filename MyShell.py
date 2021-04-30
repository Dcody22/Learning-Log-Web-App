import os 
#this line must be set up before you import django 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django 
django.setup()

#load models from MainApp
from MainApp.models import Topic, Entry 

topics = Topic.objects.all() #queary set of objects 

#select an object by a specified attribute
t = Topic.objects.get(id=1) #id is the key is the unuiqe identifief of the topic so it is used in the .get method
#in sql the above line would be written as SELECT * Entry where id = 1
print(t)
#"class_name"_set.all()
entries = t.entry_set.all() #pull all the entries associated with id =1 

for t in topics: #iterates through objects 
    print(f"Topic ID: {t.id} Topic: {t}") #text is returned since that is what is defined in the topic __str__ method
    
entries = Entry.objects.all()
for e in entries:
    print(f"Topic: {e.topic}")
    print(f"Date Posted: {e.date_added}")
    print(f"Post: {e.text}")
    
    
