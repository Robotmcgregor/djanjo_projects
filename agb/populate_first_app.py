import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agb.settings')

import django
django.setup()

# fake pop script

import random
from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()

topics = [
    'Search', 'Social', 'Marketplace', 'News', 'Games',
]

def add_topic():
    
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    
    return t

def populate(N=5):
    
    for entery in range(N):
        
        # get topic for entry
        top = add_topic()
        
        #Create fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        # Create new webpage entery
        
        webpg = Webpage.objects.get_or_create(topic= top, url=fake_url, name= fake_name)[0]
        
        
        # create a fake access record
        
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
        
if __name__ == '__main__':
    
    print('Populating script...')        
    populate(20)
    print('complete!')