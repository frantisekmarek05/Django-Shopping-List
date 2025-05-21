from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from shopping_list.models import ItemsList
from django.utils import timezone
from django.core.files.base import ContentFile
import requests
from io import BytesIO

class Command(BaseCommand):
    help = 'Adds sample items to the shopping list for a specified user'

    def handle(self, *args, **kwargs):
        # Get or create admin1 user
        user, created = User.objects.get_or_create(
            username='admin1',
            defaults={'is_staff': True, 'is_superuser': True}
        )
        if created:
            user.set_password('admin1')
            user.save()

        # Sample items with image URLs
        items = [
            {
                'name': 'Mléko',
                'category': 'dairy',
                'image_url': 'https://www.shutterstock.com/image-photo/glass-milk-isolated-on-white-260nw-556770611.jpg'
            },
            {
                'name': 'Banány',
                'category': 'vegetables',
                'image_url': 'https://www.shutterstock.com/image-photo/bunch-bananas-isolated-on-white-260nw-1722111529.jpg'
            },
            {
                'name': 'Zmrzlina',
                'category': 'frozen',
                'image_url': 'https://www.shutterstock.com/image-photo/vanilla-ice-cream-bowl-isolated-260nw-1422721266.jpg'
            },
            {
                'name': 'Pizza',
                'category': 'meal',
                'image_url': 'https://www.shutterstock.com/image-photo/tasty-pepperoni-pizza-cooking-ingredients-260nw-1259796125.jpg'
            },
            {
                'name': 'Rohlíky',
                'category': 'bread',
                'image_url': 'https://www.shutterstock.com/image-photo/fresh-baked-bread-rolls-on-260nw-1908209435.jpg'
            },
            {
                'name': 'Jogurt',
                'category': 'dairy',
                'image_url': 'https://www.shutterstock.com/image-photo/natural-yogurt-glass-jar-on-260nw-1908209435.jpg'
            },
            {
                'name': 'Jablka',
                'category': 'vegetables',
                'image_url': 'https://www.shutterstock.com/image-photo/red-apple-isolated-on-white-260nw-1727544364.jpg'
            },
            {
                'name': 'Hranolky',
                'category': 'frozen',
                'image_url': 'https://www.shutterstock.com/image-photo/french-fries-isolated-on-white-260nw-1037455708.jpg'
            }
        ]

        # Add items
        for item_data in items:
            try:
                # Create item
                item = ItemsList.objects.create(
                    user=user,
                    itemname=item_data['name'],
                    category=item_data['category'],
                    date_added=timezone.now(),
                    completed=False
                )

                # Try to download and add image
                try:
                    response = requests.get(item_data['image_url'])
                    if response.status_code == 200:
                        image_name = f"{item_data['name'].lower().replace(' ', '_')}.jpg"
                        item.image.save(image_name, ContentFile(response.content), save=True)
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"Could not download image for {item_data['name']}: {str(e)}"))

                self.stdout.write(self.style.SUCCESS(f"Successfully added item: {item_data['name']}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to add item {item_data['name']}: {str(e)}"))

        self.stdout.write(self.style.SUCCESS('Successfully added all sample items')) 