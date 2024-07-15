# Imports
from backend.application import application
from backend.guitar_parsing import parse_guitar

from data.db_sesions import main_session
from data.models import *

from flask import render_template
import pytube


@application.route('/', methods=["GET"])
def index() -> str:
    """Website index page"""

    data = dict()
    # channel = pytube.Channel("https://www.youtube.com/channel/UCNW8LgJ3hAJvfXnWZWKjrMQ")
    channel = pytube.Channel("https://www.youtube.com/c/ProgrammingKnowledge")
    videos, links = channel.videos[:3], channel.video_urls[:3]
    data["recent"] = [{"title": video.title, "link": link} for video, link in zip(videos, links)]
    data["featured"] = [parse_guitar(12), parse_guitar(13), parse_guitar(18)]

    return render_template("index.html", data=data)


@application.route('/guitars', methods=["GET"])
def guitars() -> str:
    """Website page with all guitars."""

    data = dict()

    data["guitars"] = list(map(lambda x: parse_guitar(x), main_session.query(Guitar).order_by(Guitar.id).all()))

    return render_template("guitars.html", data=data)


@application.route('/guitars/<int:guitar_id>', methods=["GET"])
def guitar(guitar_id: int) -> str:
    """Website page with single chosen guitar"""

    return render_template("guitar.html", data=parse_guitar(guitar_id)) \
        if 1 <= guitar_id <= main_session.query(Guitar).order_by(Guitar.id.desc()).first().id \
        else render_template("404.html", data={"id": guitar_id})
