from datetime import date
from python_ta.contracts import check_contracts

@check_contracts
class LocoDate:
    """ represents the location and date.
    ____________________________________________________________________________________________________________________

    Attributes:
    city: str type, represents the  city
    country: str type, represents the country
    date: type date, represents the date yyyy, mm, dd
    """
    city: str
    country: str
    date: date

    def __init__(self, year: int, month: int, day: int, city: str, country: str) -> None:
        """Initialized the object type LocoDate, with the parameters being year, month, day, city, country.
        ________________________________________________________________________________________________________________

        Precondition:
        - 0 < month <= 12
        -0 < day <= 31"""
        self.date = date(year, month, day)
        self.city = city
        self.country = country

    def __str__(self) -> str:
        """Prints the object."""
        return f"{self.date} - {self.city}, {self.country}"

    def get_date(self) ->  date:
        """Returns the date by itself."""
        return self.date

if __name__ == "__main__":
    d1 = LocoDate(2007, 11, 3, "Vladivostok", "Russia")
    d2 = LocoDate(2007, 7, 11, "Hamilton", "Canada")
    print(d1)
    print(d2)
