class NonPositiveDigitException(ValueError):
    pass

class Square():
    def __init__(self, a) -> None:
        if a <= 0:
            raise NonPositiveDigitException()
        else: 
            self.a = a