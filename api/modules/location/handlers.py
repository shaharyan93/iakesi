import os

from .models import *
from .serializers import *

from Real2D.settings import BASE_DIR
from api.commons.services import get_location_images, get_series_from_location


__all__ = [
    'get_all_locations',
    'get_countries',
    'get_prefectures',
    'get_cities',
    'get_location_detail',
    'get_location_image'
]


def get_all_locations():
    return Location.objects.all().order_by('name')


def get_countries():
    country_list = Country.objects.all().order_by('name')
    serialized_country_list = CountrySerializer(country_list, many=True)
    return dict(data=serialized_country_list.data)


def get_prefectures(country_id):
    prefecture_list = Prefecture.objects.filter(country=country_id).order_by('name')
    serialized_prefecture_list = PrefectureSerializer(prefecture_list, many=True)
    return dict(data=serialized_prefecture_list.data)


def get_cities(prefecture_id):
    city_list = City.objects.filter(prefecture=prefecture_id).order_by('name')
    serialized_city_list = CitySerializer(city_list, many=True)
    return dict(data=serialized_city_list.data)


def get_location_detail(location_id):
    try:
        location_item = Location.objects.get(id=location_id)
    except Location.DoesNotExist:
        return dict(status=404)

    serialized_location_item = LocationSerializer(location_item)
    response_data = serialized_location_item.data
    response_data['location_images'] = get_location_images(location_id)
    response_data['series'] = get_series_from_location(location_id)
    return dict(data=response_data)


def get_location_image(uuid):
    try:
        location_image_item = LocationImage.objects.get(image_name=uuid)
    except LocationImage.DoesNotExist:
        return dict(status=404)

    serialized_location_image = LocationImageSerializer(location_image_item)
    image = serialized_location_image.data['image']

    try:
        with open(os.path.join(BASE_DIR, image), mode="rb") as f:
            return dict(content=f.read(), content_type="image/jpeg")
    except TypeError or IOError:
        return dict(status=404)
