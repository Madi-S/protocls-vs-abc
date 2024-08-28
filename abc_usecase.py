from abc import ABC, abstractmethod


class FileHandler(ABC):
    def __init__(self, filename: str):
        self.filename = filename

    @abstractmethod
    def copy(self, destination: str) -> bool:
        pass

    @abstractmethod
    def remove(self) -> bool:
        pass

    @abstractmethod
    def rename(self, new_filename) -> bool:
        pass

    def write(self, text: str) -> None:
        with open(self.filename, "w") as f:
            f.write(text)

    def read(self) -> str:
        with open(self.filename, "r") as f:
            return f.read()

    def append(self, text: str) -> None:
        with open(self.filename, "a") as f:
            f.write(text)


# Inheritance is used by the way
class SoberFileHandler(FileHandler):
    def copy(self, destination: str) -> bool:
        print("Copying securely")
        return True

    def remove(self) -> bool:
        print("Removing securely")
        return True

    def rename(self, new_filename) -> bool:
        print("Renaming securely")
        return True


# Inheritance is used by the way
class DrunkFileHandler(FileHandler):
    def copy(self, destination: str) -> bool:
        print("coPying fiL3")
        return True

    def remove(self) -> bool:
        print("reeM0ving FI le")
        return True

    def rename(self, new_filename) -> bool:
        print("ugh ... renaming ugh ... fileee")
        return True


if __name__ == "__main__":
    sfh = SoberFileHandler("somefile.txt")
    sfh.copy("new_somefile.txt")
    sfh.write("hello")
    sfh.remove()
    assert isinstance(sfh, FileHandler)
    assert isinstance(sfh, SoberFileHandler)

    dfh = DrunkFileHandler("whiskey.txt")
    dfh.rename("vodka.txt")
    dfh.write("lesss go")
    dfh.remove()
    assert isinstance(dfh, FileHandler)
    assert isinstance(dfh, DrunkFileHandler)
