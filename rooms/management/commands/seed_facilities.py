from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "This command creates facilities"

    def handle(self, *args, **options):
        facilities = [
            "건물 내 무료 주차",
            "헬스장",
            "자쿠지",
            "수영장",
            "헬스장",
            "엘리베이터",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS("시설 생성완료!"))
