# Imports
from data.db_sesions import main_session
from data.models import *


def parse_guitar(guitar: Guitar | int) -> dict:
    """Gathers all data about guitar that matches given `guitar`."""
    result = dict()

    if isinstance(guitar, int):
        guitar = main_session.query(Guitar).filter(Guitar.id == guitar).first()
    result["id"] = guitar.id
    result["title"] = f"Guitar №{guitar.id}"
    result["years"] = guitar.years
    result["info"] = guitar.info
    result["stats"] = {
        "Guitar type": main_session.query(GuitarType).filter(GuitarType.id == guitar.guitar_type_id).first().type,
        "Wood type": main_session.query(WoodType).filter(WoodType.id == guitar.wood_type_id).first().type,
        "Body type": main_session.query(BodyType).filter(BodyType.id == guitar.body_type_id).first().type,
        "Bridge type": main_session.query(BridgeType).filter(BridgeType.id == guitar.bridge_type_id).first().type,
        "Pickups": [
            main_session.query(PickupType).filter(PickupType.id == pickup.pickup_id).first().type
            for pickup in main_session.query(Pickups).filter(Pickups.guitar_id == guitar.id).order_by(Pickups.id).all()
        ]
    }

    images_folder = "assets/guitars/"
    images = list(map(
        lambda x: images_folder + x.image_filename,
        main_session.query(Image).filter(Image.guitar_id == guitar.id).order_by(Image.is_icon.desc()).all()
    ))

    result["icon"] = images[0]
    result["images"] = images

    return result
