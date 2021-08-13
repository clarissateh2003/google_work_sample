"""A video library class."""

from .video import Video
from pathlib import Path
import csv


# Helper Wrapper around CSV reader to strip whitespace from around
# each item.
def _csv_reader_with_strip(reader):
    yield from ((item.strip() for item in line) for line in reader)


class VideoLibrary:
    """A class used to represent a Video Library."""

    def __init__(self):
        """The VideoLibrary class is initialized."""
        self._videos = {}
        with open(Path(__file__).parent / "videos.txt") as video_file:
            reader = _csv_reader_with_strip(
                csv.reader(video_file, delimiter="|"))
            for video_info in reader:
                title, url, tags = video_info
                self._videos[url] = Video(
                    title,
                    url,
                    [tag.strip() for tag in tags.split(",")] if tags else [],
                )

    def get_all_videos(self):
        """Returns ONLY VALUES of the video information from the video library."""
        return list(self._videos.values())

    def get_video_information(self):
        """Returns an alphabetically sorted list of VIDEO IDs from the video library."""
        #this returns a list of video IDs STRINGS sorted in alphabetical order
        video_list = sorted(list(self._videos))

        #empty list to store each object
        #video_object_list = []

        #for video in video_list:
        #    video_object_list.append(self.get_video(video))
        #    video_object_list.append(video.title)

        return video_list
        #return list(self._videos.title, "(" + self._videos.video_id + ")", "[" + self._videos.tags + "]")

    def get_video(self, video_id):
        """Returns the video object (title, url, tags) from the video library.

        Args:
            video_id: The video url.

        Returns:
            The Video object for the requested video_id. None if the video
            does not exist.
        """
        return self._videos.get(video_id, None)
