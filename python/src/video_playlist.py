"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playlist_title: str):
        """Video constructor."""
        self._title = playlist_title
        self._video_list = []

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        #self._tags = tuple(video_tags)

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    #@property
    #def video_list(self) -> Sequence[str]:
     #   """Returns the video ids of all the videos in the playlist."""
      #  return self._video_list

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video id to the playlist."""

        for video in self._video_list:
            # to ensure search function is not case sensitive
            if video.lower() == video_id.lower():
                print("Cannot add video to " + playlist_name +": Video already added")
                return 

        self._video_list.append(video_id.lower())

        # strip is to remove whitespace
        #print("Added video to " + playlist_name +": " + video_id.strip())
        return

