from abc import ABC, abstractmethod

# Interface
class IHuman(ABC):
    @abstractmethod
    def _wake_up(self):
        """Wake up from sleep."""
        pass

    @abstractmethod
    def _sell_treasures(self):
        """Sell existing treasures."""
        pass

    @abstractmethod
    def _sleep(self):
        """Sleep after the day."""
        pass
