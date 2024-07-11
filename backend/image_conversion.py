# Imports
from io import BytesIO
from PIL import Image


def image_to_bytes(image: Image) -> bytes:
    """Converts `pillow` image to `bytes` which can then be saved in database."""
    bytebuf = BytesIO()
    image.save(bytebuf, format="PNG")
    bytes_ = bytebuf.getvalue()
    return bytes_


def bytes_to_image(bytes_: bytes) -> Image:
    """Converts `bytes` to `pillow` image."""
    return Image.open(BytesIO(bytes_))
