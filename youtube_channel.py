class YouTubeChannel:
    def __init__(self, name: str="", video_count: int=0):
        self._name = name
        self.__video_count = video_count

    def __str__(self) -> str:
        return f"Channel: {self._name}, Videos: {self.__video_count}"
    
    def set_name(self, name: str):
        self._name = name
    
    def get_name(self) -> str:
        return self._name
    
    def set_VC(self, video_count: int):
        self.__video_count = video_count

    def get_VC(self) -> int:
        return self.__video_count

def main():
    channel = YouTubeChannel("UVUCS1410", 150)
    print(channel)
    channel.set_name("New Channel")
    channel.set_VC(124)
    print(channel)
    print(channel.get_name())
    print(channel.get_VC())
    channel._name = "name"
    print(channel.get_name())
    channel._YouTubeChannel__video_count = 100
    print(channel.get_VC())

if __name__ == "__main__":
    main()
