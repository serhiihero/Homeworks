from abc import ABC, abstractmethod

# Interface
class IDiver(ABC):
    @abstractmethod
    def _move_to_the_point(self, x, y):
        """Move to the specified point."""
        pass

    @abstractmethod
    def collect_treasures(self, x, y):
        """Collect treasures at the specified point."""
        pass

    @abstractmethod
    def _immersion(self):
        """Immerse into the water."""
        pass
