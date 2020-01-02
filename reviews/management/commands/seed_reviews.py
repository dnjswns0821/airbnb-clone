import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_model
from users import models as user_model
from rooms import models as room_model


class Command(BaseCommand):

    help = "This command creates reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many reviews do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_model.User.objects.all()
        rooms = room_model.Room.objects.all()
        seeder.add_entity(review_model.Review, number, {
            'accuracy': lambda x: random.randint(0, 6),
            'communication': lambda x: random.randint(0, 6),
            'cleanliness': lambda x: random.randint(0, 6),
            'location': lambda x: random.randint(0, 6),
            'check_in': lambda x: random.randint(0, 6),
            'value': lambda x: random.randint(0, 6),
            'room' : lambda x: random.choice(rooms),
            'user' : lambda x: random.choice(users),
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} 리뷰 생성완료!"))
