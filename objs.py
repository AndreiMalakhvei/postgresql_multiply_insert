from datetime import datetime
from static_fields import *


class Obj:
    def __init__(self, link=None, reference=None, price=None, title=None, description=None, pubdate=None,
                 areas=None, city=None, address=None, region=None, rooms=None, exyear=None, objhash=None,
                 seller=None, photo_links=None, photo_qty=None):
        self.link = link
        self.reference = reference
        self.price = price
        self.title = title
        self.description = description
        self.pubdate = pubdate
        self.areas = areas
        self.city = city
        self.address = address
        self.region = region
        self.rooms = rooms
        self.exyear = exyear
        self.objhash = objhash
        self.seller = seller
        self.photo_links = photo_links
        self.photo_qty = photo_qty


def create_obj_list(qty):
    obj_list = []
    for x in range(qty):
        new_obj = Obj(
            link=x, reference=REFERENCE, price=PRICE, title=TITLE, description=LONG_TEXT, pubdate=datetime.now(),
            areas=AREAS, city=CITY, address=ADDRESS, region=REGION, rooms=ROOMS, exyear=EXYEAER, seller=SELLER,
            photo_links=PHOTO_LINKS, photo_qty=PHOTO_QTY
        )
        obj_list.append(new_obj)
    return obj_list


def create_tuple_list(qty):
    tup_list = []
    for x in range(qty):
        new_tup = (x, REFERENCE, PRICE, TITLE, LONG_TEXT, datetime.now(), AREAS, CITY, ADDRESS, REGION, ROOMS, EXYEAER,
                   SELLER, PHOTO_LINKS, PHOTO_QTY)
        tup_list.append(new_tup)
    return tup_list

