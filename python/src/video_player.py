"""A video player class."""

from .video_library import VideoLibrary
#import .video
import random 
from .video_playlist import Playlist

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

        #stores the currently playing video id
        self._current_playing = None

        #stores whether a video is paused
        self._current_paused = False

        #stores all existing playlist NAMES in a list
        self._playlist_library = []

        #stores all existing playlist INFORMATION in a dictionary
        self._playlist_information = {}

    #def get_current_playing(self):
        #fetches the video object using the id of the video currently being played
    #    return self._video_library.get_video(self._current_playing)
    
    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")
    
    def show_all_videos(self):
        """Returns all videos."""

        # to separate each tag with a space
        separator = " "
        
        print("Here's a list of all available videos:")
        
        for video_id in self._video_library.get_video_information():
            video_object = self._video_library.get_video(video_id) 
            # converts the tuple of tags to a list of tags, removes the () brackets and
            video_tags = [tag.strip() for tag in video_object.tags] 
            print(
                video_object.title, 
                "("+ video_object.video_id + ")", 
                
                # if else gives it a value on a condition. like if there are no tags
                # joins all of the video tags to remove the commas, uses a space " " as a separator
                "["+separator.join(video_tags)+"]" if video_object.tags else []
                #[tag.strip() for tag in video_object.tags.split(",")] if video_object.tags else []
                #[tag.strip() for tag in tags.split(",")] if tags else []
            )
        
        #for video_id in self._video_library.get_formatted_video_information():
         #   print(video_id)
        # this prints the list of all video IDs in alphabetical order
        #for video in self._video_library.get_video_information():
         #   print(video) 
            
        
        #for video in self._video_library.get_all_videos():
         #   print(video) 
        
        #video.title(self)
        #print(sorted_videos)
        #sorted_videos.sort()

        #print("Here's a list of all available videos:")
        #for video in sorted_videos:
        #    print(video)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        # fetches an object of the Video class (see video.py)
        video_object = self._video_library.get_video(video_id)
        #print(type(video))
        video_current_playing = self._video_library.get_video(self._current_playing)

        if video_object is None:
            print("Cannot play video: Video does not exist")
            return

        elif self._current_playing == None:
            print("Playing video: " + video_object.title)
            self._current_playing = video_id
            self._current_paused = False
            return

        else:
        # this one is to change video if it's a different ID
        #elif self._current_playing != video_id:
            print("Stopping video: " + video_current_playing.title)
            print("Playing video: " + video_object.title)
            self._current_playing = video_id
            self._current_paused = False
            return
        
        #self._current_playing = video_id

    def stop_video(self):
        """Stops the current video."""
        
        #fetches the video object using the id of the video currently being played
        video_current_playing = self._video_library.get_video(self._current_playing)

        if self._current_playing == None:
            print("Cannot stop video: No video is currently playing")
            return

        else:
            print("Stopping video: " + video_current_playing.title)
            self._current_playing = None
            return

    def play_random_video(self):
        """Plays a random video from the video library."""
        #fetches the video object using the id of the video currently being played
        video_current_playing = self._video_library.get_video(self._current_playing)

        if self.number_of_videos == 0:
            print("No videos available.")
            return

        else:
            # chooses a random video id from the list of video ids
            random_video_id = random.choice(self._video_library.get_video_information())
            self.play_video(random_video_id)
            return

    def pause_video(self):
        """Pauses the current video."""
        #fetches the video object using the id of the video currently being played
        video_current_playing = self._video_library.get_video(self._current_playing)

        if self._current_playing == None:
            print("Cannot pause video: No video is currently playing")
            return

        elif self._current_paused == True:
            print("Video already paused: " + video_current_playing.title)
            return
        
        else:
            print("Pausing video: " + video_current_playing.title)
            self._current_paused = True
            return

    def continue_video(self):
        """Resumes playing the current video."""

        #fetches the video object using the id of the video currently being played
        video_current_playing = self._video_library.get_video(self._current_playing)

        if self._current_playing == None:
            print("Cannot continue video: No video is currently playing")
            return
        
        elif self._current_paused == False:
            print("Cannot continue video: Video is not paused")
            return

        else:
            print("Continuing video: " + video_current_playing.title)
            self._current_paused = False
            return
        

    def show_playing(self):
        """Displays video currently playing."""
        #fetches the video object using the id of the video currently being played
        video_current_playing = self._video_library.get_video(self._current_playing)

        # to separate each tag with a space
        separator = " "

        if self._current_playing == None:
            print("No video is currently playing")
            return
        
        elif self._current_paused == True:
            # to convert the tuple of video tags into a list
            video_tags = [tag.strip() for tag in video_current_playing.tags] 

            print("Currently playing:", 
            video_current_playing.title,
            "("+ video_current_playing.video_id + ")", 
                
                # if else gives it a value on a condition. like if there are no tags
                # joins all of the video tags to remove the commas, uses a space " " as a separator
                "["+separator.join(video_tags)+"]" if video_current_playing.tags else []
                , "- PAUSED"
            )
            return

        else:
            # to convert the tuple of video tags into a list
            video_tags = [tag.strip() for tag in video_current_playing.tags] 

            print("Currently playing:", 
                video_current_playing.title,
                "("+ video_current_playing.video_id + ")", 
                    
                    # if else gives it a value on a condition. like if there are no tags
                    # joins all of the video tags to remove the commas, uses a space " " as a separator
                    "["+separator.join(video_tags)+"]" if video_current_playing.tags else []
                )
            return

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for playlist in self._playlist_library:
            # to ensure search function is not case sensitive
            if playlist.lower() == playlist_name.lower():
                print("Cannot create playlist: A playlist with the same name already exists")
                return 

        # add the name of the playlist to a list
        self._playlist_library.append(playlist_name)

        # create an object of class playlist and add it to the dictionary of playlists
        self._playlist_information[playlist_name.lower()] = Playlist(playlist_name)

        # strip is to remove whitespace
        print("Successfully created new playlist: " + playlist_name.strip())
        
        return

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if self._playlist_library == []:
            print("Cannot add video to " + playlist_name + ": Playlist does not exist")
            return

        for playlist in self._playlist_library:
            # to ensure search function is not case sensitive
            if playlist.lower() == playlist_name.lower():
                break 
            #elif playlist == None:
             #   print("Cannot add video to " + playlist_name + ": Playlist does not exist")
              #  return
            else:
                print("Cannot add video to " + playlist_name + ": Playlist does not exist")
                return

        # fetches an object of the Video class (see video.py)
        video_object = self._video_library.get_video(video_id)

        # check if video_id exists
        if video_object is None:
            print("Cannot add video to " + playlist_name + ": Video does not exist")
            return

        #get the playlist object using the key of playlist_name
        playlist = self._playlist_information[playlist_name.lower()]

        # checks if video has already been added to playlist
        for video in playlist._video_list:
            if video == video_id:
                print("Cannot add video to " + playlist_name + ": Video already added")
                return

        else:
            #self._playlist_information.add_to_playlist(playlist_name, video_id)
            print("Added video to " + playlist_name + ": " + video_object.title)

            playlist.add_to_playlist(playlist_name, video_id)
            return

 

    def show_all_playlists(self):
        """Display all playlists."""

        if self._playlist_library == []:
            print("No playlists exist yet")
            return

        else:
            print("Showing all playlists:")
            sorted_playlists = sorted(self._playlist_library)
            for playlist in sorted_playlists:
            # to ensure search function is not case sensitive
                print(playlist)
            return 

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
