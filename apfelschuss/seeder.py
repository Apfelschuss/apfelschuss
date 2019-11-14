import random
import time
from django.contrib.auth import get_user_model
from django.utils import timezone

from faker import Faker

from apfelschuss.polls.models import Category, Poll

fake = Faker()
User = get_user_model()


def seed_users(num_entries=10, overwrite=False):
    """
    Creates num_entries worth a new users
    """
    if overwrite:
        print("Overwriting Users")
        User.objects.all().delete()
    count = 0
    for _ in range(num_entries):
        first_name = fake.first_name()
        last_name = fake.last_name()
        u = User.objects.create_user(
            name=first_name + ' ' + last_name,
            first_name=first_name,
            last_name=last_name,
            email=first_name + "." + last_name + "@fakermail.com",
            username=first_name + last_name,
            password="password"
        )
        count += 1
        percent_complete = count / num_entries * 100
        print(
                "Adding {} new Users: {:.2f}%".format(num_entries, percent_complete),
                end='\r',
                flush=True
                )
    print()


def seed_categories(num_entries=10, choice_min=2, choice_max=5, overwrite=False):
    """
    Seeds num_entries category with random users as owners
    """
    if overwrite:
        print('Overwriting category')
        Category.objects.all().delete()
    users = list(User.objects.all())
    count = 0
    for _ in range(num_entries):
        if count % 5 == 0:
            status = 'draft'
        else:
            status = 'published'  
        c = Category( 
            title = fake.sentence(),
            status = status,
            poll_date = timezone.now(),
            owner = random.choice(users),
        )
        c.save()
        count += 1
        percent_complete = count / num_entries * 100
        print(
                "Adding {} new Polls: {:.2f}%".format(num_entries, percent_complete),
                end='\r',
                flush=True
                )
    print()


def seed_all(num_entries=10, overwrite=False):
    """
    Runs all seeder functions. Passes value of overwrite to all
    seeder function calls.
    """
    start_time = time.time()
    # run seeds
    seed_users(num_entries=num_entries, overwrite=overwrite)
    seed_categories(num_entries=num_entries, overwrite=overwrite)
    # seed_votes()
    # get time
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print("Script Execution took: {} minutes {} seconds".format(minutes, seconds))
