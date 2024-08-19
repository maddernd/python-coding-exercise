from coding_exercise.domain.model.cable import Cable
from typing import List

class Splitter:

    def __validate(self, cable: Cable, num_splits: int):
        if not 1 <= num_splits <= 64:
            raise ValueError("Times must be between 1 and 64.")
        if not 2 <= cable.length <= 1024:
            raise ValueError("Cable length can only be between 2 and 1024.")

    def split(self, cable: Cable, num_splits: int) -> List[Cable]:
        self.__validate(cable, num_splits)

        segment_length = cable.length // num_splits
        remaining_length = cable.length % num_splits

        if segment_length < 1:
            raise ValueError("Cannot split the cable segments less than 1")

        segments = [Cable(segment_length, f"{cable.name}-{i:02}") for i in range(num_splits)]

        for i in range(remaining_length):
            segments[i].length += 1

        return segments
