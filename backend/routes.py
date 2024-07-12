# Imports
from backend.application import application

from flask import render_template
import pytube


@application.route('/', methods=["GET"])
def index():
    """Website index page"""

    data = dict()
    # channel = pytube.Channel("https://www.youtube.com/channel/UCNW8LgJ3hAJvfXnWZWKjrMQ")
    channel = pytube.Channel("https://www.youtube.com/c/ProgrammingKnowledge")
    videos, links = channel.videos[:3], channel.video_urls[:3]
    data["recent"] = [{"title": video.title, "link": link} for video, link in zip(videos, links)]

    return render_template("index.html", data=data)
