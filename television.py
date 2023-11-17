class Television:
    """
    A class representing details for a television object.
    """
    MIN_VOLUME = 0  # Minimum volume constant.
    MAX_VOLUME = 2  # Maximum volume constant.
    MIN_CHANNEL = 0  # Minimum channel constant.
    MAX_CHANNEL = 3  # Maximum channel constant

    def __init__(self) -> None:
        """
        Method to set default values of a television object.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to modify the status of the television.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method to modify the mute when the television is on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Method to increase the channel when the television is on.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
                Method to decrease the channel when the television is on.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
                Method to increase the volume and modify mute when the television is on.
        """
        if self.__status and self.__volume < Television.MAX_VOLUME:
            self.__muted = False
            self.__volume += 1

    def volume_down(self) -> None:
        """
                Method to decrease the volume and modify mute when the television is on.
        """
        if self.__status and self.__volume > Television.MIN_VOLUME:
            self.__muted = False
            self.__volume -= 1

    def __str__(self) -> str:
        """
        Formats a string for the television object depending on mute.
        :return: String depending on mute.
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
