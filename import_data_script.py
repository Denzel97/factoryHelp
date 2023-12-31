import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'factoryHelp.settings')

import django
django.setup()

import json
from app.models import Company


def import_data_from_json(json_file_path_data):
    with open(json_file_path_data, 'r') as file:
        data = json.load(file)

    for entry in data:
        # Create an instance of the Company model and populate its fields
        instance = Company(
            page_name=entry['page_name'],
            logo_colour=entry['logo_colour'],
            logo_country_name=entry['logo_country_name'],
            logo_country_flag=entry['logo_country_flag'],
            logo_image=entry.get('logo_image', ''),
        )
        try:
            instance.save()
            print(f"Saved entry: {entry}")
        except Exception as e:
            print(f"Failed to save entry: {entry}. Exception: {e}")


if __name__ == "__main__":
    json_file_path = 'C:/Users/Administrator/Desktop/Scraping/Logo Pages/Logo Pages/scraped_data.json'
    import_data_from_json(json_file_path)
