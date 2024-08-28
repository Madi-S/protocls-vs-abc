from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


@runtime_checkable
class Author(Protocol):
    def write(self, text: str) -> None:
        pass


@runtime_checkable
class Reader(Protocol):
    def read(self) -> str:
        pass


# What about that, huh?
def write_something(writer: Author, text: str) -> None:
    writer.write(text)


def read_something(reader: Reader) -> None:
    return "lorem inpsum"


# See? No inheritance here by the way
# No direct relation with Author
# It just happens to know AUthor's abstract methods
# Well, it is save enough, because it is checked in runtime -> error, can be
class ThomasWolfe:
    def __init__(self):
        self.name = "Thomas Wolfe"

    def write(self, text: str) -> None:
        print("I am writing a new novel ...")


# Wow, not here too
class JohnDoe:
    def read(self):
        print("I am reading something")


class Dude(ABC):
    @abstractmethod
    def write(self, text: str) -> None:
        pass


class SomeSpecificDude(Dude):
    def write(self, text: str) -> None:
        print(f'Some specific dude is writing ... {text} ...')


class Dostoevsky:
    def write(self, text: bytes) -> None:
        print("I am writing a novel but in bytes ...")


if __name__ == "__main__":
    writer = ThomasWolfe()
    reader = JohnDoe()
    text = "Hello t.Protocol"

    write_something(writer, text)
    read_something(reader)

    # NOTE: gonna fail without runtime_checkable
    assert isinstance(SomeSpecificDude, Author)

    # NOTE: going to work, however, why so?
    # well, protocols do not operate in-depth checks
    # obviously, Doestoevsky should not be an instance of Writer
    # because it has a different argument type
    assert isinstance(Dostoevsky, Writer)

    # NOTE: also your code editor might mark line #75 as unreachable
    # but that is not true, it will be reachable, duh, type checking with protocols :D
