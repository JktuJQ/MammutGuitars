# Imports
from data.db_sesions import databases


# guitars.sqlite
Guitar = None
Image = None
GuitarType = None
WoodType = None
BodyType = None
BridgeType = None
PickupType = None
Pickups = None


def load_models():
    """Loads all models from databases"""
    global Guitar, Image, GuitarType, WoodType, BodyType, BridgeType, PickupType, Pickups

    guitars_database = databases["guitars"].classes

    Guitar = guitars_database.guitars
    Image = guitars_database.images
    GuitarType = guitars_database.guitar_types
    WoodType = guitars_database.wood_types
    BodyType = guitars_database.body_types
    BridgeType = guitars_database.bridge_types
    PickupType = guitars_database.pickup_types
    Pickups = guitars_database.pickups
