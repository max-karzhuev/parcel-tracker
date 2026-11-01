from python_ta.contracts import check_contracts
from loco_date import LocoDate
from datetime import date


class WrongPackageTypeError(Exception):
    """Exception raised when trying to classify a Package as a wrong sub-class object."""

    def __str__(self) -> str:
        """Return string representation of this error"""
        return "Wrong sub-class!"

class IncompletePackageInfoError(Exception):
    """Exception raised when using a method on a Package subclass objects without having the instance attributes
    completed"""

    def __str__(self) -> str:
        """Return string representation of this error"""
        return "Package info is inclomplete!"

@check_contracts
class Package:
    """Represents an super-class of all packages being delivered.
    ____________________________________________________________________________________________________________________
    Attributes:
    - _departure: object type LocoDate. Contains the date(yyyy, mm, dd) followed by the city, and country of the
        departure of the package. Initially set to "not set"
    - _arrival: object type LocoDate. Contains the date(yyyy, mm, dd) followed by the city, and country of the
        arrival of the package. Initially set to "not set"
    - sender: object type str. Contains the name of the sender of the package.
    - recipient: object type str. Contains the name of the recipient of the package.
    - tracking_number: onject type str. Contains the unique shipping alphanumberic code for tracking the pakage.
    - carrier: object typpe str. Name of the carrier that issued the tracking number.
    ____________________________________________________________________________________________________________________
    Representation Invariants:
    - 10 <= len(self.tracking_number) <= 24
    """
    _departure: LocoDate | str
    _arrival: LocoDate | str
    sender: str
    recipient: str
    tracking_number: str
    carrier: str

    def __init__(self, sender: str, recipient: str, tracking_number: str, carrier: str) -> None:
        """Initilizes the object type Package. Sets _departure and _arrival to "not set"
        ________________________________________________________________________________________________________________
        Preconditions:
        - 10 <= len(tracking_number) <= 24
        """
        self._departure = "not set"
        self._arrival = "not set"
        self.sender = sender
        self.recipient = recipient
        self.tracking_number = tracking_number
        self.carrier = carrier

    def __str__(self) -> str:
       """Returns the description of the package as a str."""
       return (
            f"\n___________________________________________________________\n"
            f"Tracking number: {self.tracking_number}\n"
            f"Sender: {self.sender}\n"
            f"Departure: {self._departure}\n"
            f"Recipient: {self.recipient}\n"
            f"Arrival: {self._arrival}\n"
            f"Carrier: {self.carrier}"
            f"\n___________________________________________________________\n"
       )

    def set_departure(self, year: int, month: int, day: int, city: str, country: str) -> None:
        """Method sets the departure date and location.
        ________________________________________________________________________________________________________________
        Preconditions:
        - 0 < month <= 12
        - 0 < day <= 31
        """
        type_check = (isinstance(year, int) and isinstance(month, int) and isinstance(day, int) and isinstance(city, str)
                      and isinstance(country, str))
        if not type_check:
            try:
                year = int(year)
                month = int(month)
                day = int(day)
                city = str(city)
                country = str(country)
            except TypeError:
                print("Invalid dates! Please try again.")
        departure = LocoDate(year, month, day, city, country)
        self._departure = departure

    def set_arrival(self, year: int, month: int, day: int, city: str, country: str) -> None:
        """Method sets the arrival date and location.
        ________________________________________________________________________________________________________________
        Preconditions:
        - 0 < month <= 12
        - 0 < day <= 31
        """
        type_check = (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)
                       and isinstance(city, str) and isinstance(country, str))
        if not type_check:
            try:
                year = int(year)
                month = int(month)
                day = int(day)
                city = str(city)
                country = str(country)
            except TypeError:
                print("Invalid dates! Please try again.")
        arrival = LocoDate(year, month, day, city, country)
        self._arrival = arrival

    def is_domestic(self) -> bool | None:
        """Method checks if the shipment is domestic(True) or internartional(False)"""
        if isinstance(self._departure, LocoDate) and isinstance(self._arrival, LocoDate):
            return self._departure.country == self._arrival.country
        else:
            raise IncompletePackageInfoError

    def transit_days(self) -> int:
        """Returns the number of days the package is expected to be in trasit given the current departure and arrival info.
        Preconditions:
        - self._arrival is set
        - self._departure is set
        - self.get_departure() <= self.get_arrival()"""
        if isinstance(self._arrival, LocoDate) and isinstance(self._departure, LocoDate):
            transit_time = int((self._arrival.date - self._departure.date).days)
        else:
            raise IncompletePackageInfoError
        return transit_time

@check_contracts
class Letter(Package):
    """Represents a class of letters which is a sub-class to Package. The letters are classified based on their size,
    while the specific dimensions are disregarded as irrelevant. Additionally they are classified on weight aswell.
      They have the same atributes as Package.
    ____________________________________________________________________________________________________________________
    Attributes:
    - _departure: object type LocoDate. Contains the date(yyyy, mm, dd) followed by the city, and country of the
        departure of the package. Initially set to "not set"
    - _arrival: object type LocoDate. Contains the date(yyyy, mm, dd) followed by the city, and country of the
        arrival of the package. Initially set to "not set"
    - mailer: object type str. Contains the name of the sender of the package.
    - recipient: object type str. Contains the name of the recipient of the package.
    - tracking_number: onject type str. Contains the unique shipping alphanumberic code for tracking the pakage.
    - carrier: object typpe str. Name of the carrier that issued the tracking number.
    -type: object type str. It is classified between "standard" and "non-standard" lettermail.
    ____________________________________________________________________________________________________________________
    Representation Invariants:
    - self.type in {"standard", "non-standard", "not set", "not a letter"}
    - 10 <= len(self.tracking_number) <= 24
    """
    type: str

    def __init__(self, dyear: int, dmonth: int, dday: int, dcity: str, dcountry: str, ayear: int, amonth: int,
                 aday: int, acity: str, acountry: str, sender: str, recipient: str,
                 tracking_number: str, carrier: str, length: int, width: int, thickness: int, weight: int) -> None:
        """Initilizes the object type Letter. ".
        ________________________________________________________________________________________________________________
        Preconditions:
        - 10 <= len(tracking_number) <= 24
        """
        Package.__init__(self, sender, recipient, tracking_number, carrier)
        self.set_departure(dyear, dmonth, dday, dcity, dcountry)
        self.set_arrival(ayear, amonth, aday, acity, acountry)
        self.set_type(length, width, thickness, weight)

    def set_type(self, length: int, width: int, thickness: int, weight: int) -> None:
        """Sets the instance attribute of type to ""standard", "non-standard" or "not a letter". Compares the dimensions
        ofthe letter with the regulations. The length,width, and thickness are measured in millimeters and must be
        roundedto the nearest millimeter. The weight ismeasured in grams and must be rounded to the nearest gram.
        ________________________________________________________________________________________________________________
        Preconditions:
        - 0 < length
        - 0 < width
        - 0 < thickness
        - 0 < weight
        """
        standard_length = 140 <= length <= 245
        standard_width = 90 <= width <= 156
        standard_thickness = 0 <= thickness <= 5
        standard_weight = 2 <= weight <= 50
        non_standard_length = 140 <= length <= 380
        non_standard_width = 90 <= width <= 270
        non_standard_thickness = 0 <= thickness <= 20
        non_standard_weight = 3 <= weight <= 500
        # Since the Non-standard letter range contains the entirety of of the Standard letter range, we need to ensure
        # that at least one of the measurements is out of range of Standard mail.
        filter_criteria = (not standard_width or not standard_weight or not standard_thickness or not standard_length)

        # For standard mail all standard_... variables must be true.
        if standard_length and standard_thickness and standard_weight and standard_width:
            self.type = "standard"
        elif (non_standard_length and non_standard_thickness and non_standard_weight and non_standard_width
                 and filter_criteria):
            self.type = "non-standard"
        else:
            self.type = "not a letter"
            raise WrongPackageTypeError


@check_contracts
class Parcel(Package):
    """Represents the class for apckages that are not letter mail due to weight and dimension not aligning witht the
    standard. For this type of package the dimensions size and weight matters.
    ____________________________________________________________________________________________________________________
    Attributes:
    - _departure: object type LocoDate. Contains the date(yyyy, mm, dd) followed by the city, and country of the
        departure of the package.
    - _arrival: object type LocoDate. Contains the date(yyyy, mm, dd) followed by the city, and country of the
        arrival of the package.
    - mailer: object type str. Contains the name of the sender of the package.
    - recipient: object type str. Contains the name of the recipient of the package.
    - tracking_number: onject type str. Contains the unique shipping alphanumberic code for tracking the pakage.
    - carrier: object typpe str. Name of the carrier that issued the tracking number.
    - size: tuple(int, int, int). A tuple of three ints represending height, width, length dimensions in millimeter.
    - weight: object type int. Represents the weight of the parcel in grams.
    ____________________________________________________________________________________________________________________
    Representation Invariants:
    - 10 <= len(self.tracking_number) <= 24
    - for i in size:
        0 < i == True
    - 0 < weight
    """
    weight: int
    size: tuple

    def __init__(self, dyear: int, dmonth: int, dday: int, dcity: str, dcountry: str, ayear: int, amonth: int,
                aday: int, acity: str, acountry: str, sender: str, recipient: str, tracking_number: str, carrier: str,
                height: int, width: int, length: int, weight: int) -> None:
        """Initilizes the object Parcel. the weight and size is set to "not set" intially
        ________________________________________________________________________________________________________________
        Preconditions:
        - 10 <= len(tracking_number) <= 24
        """
        Package.__init__(self, sender, recipient, tracking_number, carrier)
        self.set_departure(dyear, dmonth, dday, dcity, dcountry)
        self.set_arrival(ayear, amonth, aday, acity, acountry)
        self.set_size(height, width, length)
        self.set_weight(weight)

    def set_size(self, height: int, width: int, length: int) -> None:
        """Sets the size of the parcel. Inputs the dimenstions of height, width, length in millimeters.
        ________________________________________________________________________________________________________________
        Precodnitions:
        - 0 =< height
        - 0 =< width
        - 0 =< length
        """
        size = (height, width, length)
        self.size = size

    def set_weight(self, weight: int) -> None:
        """Sets the weight of the parcel. Inputs the weight in grams.
        ________________________________________________________________________________________________________________
        Preconditions:
        - 0 =< weight
        """
        self.weight = weight

    def volume(self) -> int:
        """Returns the volume of the parcel in cubic centimeters.
        Preconditions: Size is set.
        """
        vol = (self.size[0] * self.size[1] * self.size[2]) // 1000
        if vol == 0:
            raise IncompletePackageInfoError
        return vol



@check_contracts
class ShipmentList:
    """Represents a shipment list ordered by delivery date.
    ____________________________________________________________________________________________________________________
    Attributes:
    - _shipments: an object of type dict{str : Package}. It is a dictionary with order numbers as keys and packages as
    values.
    - shipment_list: an object type list[tuple(date, str)]. The date will be the arrival date of the shipment and the
    str will be the corresponding shipment number.
    - active_shipments: object type int. The integer represents the number of tuples the shipment_list has, which
    represents the number of active shipments.
    ____________________________________________________________________________________________________________________
    Representation Invariants
    - self.active_shipments == len(self._shipment_list) == len(self._shipments)
    """
    #CONSTANTS:
    DATE = 0
    NUM = 1

    _shipments: dict
    _shipment_list: list
    active_shipments: int

    def __init__(self) -> None:
        """Initializes object type ShipmentList. Initially _shipments and shipment_list are empty while
        active_shipments is zero."""
        self._shipments = {}
        self._shipment_list = []
        self.active_shipments = 0

    def is_empty(self) -> bool:
        """Returns whether the list is empty."""
        return self.active_shipments == 0

    def enqueue(self, package: Package) -> None:
        """Adds an order to the shipments list and shipments.
        ________________________________________________________________________________________________________________
        Preconditions:
        - Package._arrival != "not set"
        - Package.tracking_number != "not set"
        """
        if isinstance(package._arrival, LocoDate):
            tracking_number = package.tracking_number
            arrival = package._arrival.date
        else:
            raise IncompletePackageInfoError

        tracking_number = package.tracking_number
        shipment_list_node = (arrival, tracking_number)

        #Add the shipment to the shipments.
        self._shipments[tracking_number] = package

        #Insert the shipment in the proper arrival chronoligical order.
        if self._shipment_list == []:
            #If it is the first shipment we can just append it.
            self._shipment_list.append(shipment_list_node)
        else:
            #We must find the correct index for the shipment.
            i = 0
            while i < len(self._shipment_list) and self._shipment_list[i][0] <= arrival:
                i += 1
            self._shipment_list.insert(i, shipment_list_node)

        self.active_shipments += 1

    def deliver(self, date) -> list[Package]:
        """Returns the list of all packages being delivered on the date. Mutates the _shipment_list and _shipments to
        remove the packages that have date as their arrival date 'deliver' them.
        ________________________________________________________________________________________________________________
        Preconditions:
        - no package inside the lists can have an arrival date earlier then the input date, as they would have been
        already delivered
        """
        delivery_list = []
        for item in self._shipment_list[:]:

            #Extrack the package object
            tracking_number = item[self.NUM]
            package = self._shipments[tracking_number]

            if date == item[self.DATE]:
                delivery_list.append(package)
                #Delete the package from the _shipments and _shipments_list.
                del self._shipments[tracking_number]
                self._shipment_list.remove(item)
                self.active_shipments -= 1
            #B/c in chronological order, we can terminate the list as soon as item's date is after the date
            elif date < package._arrival.date:
                break

        return delivery_list

    def check_scheduled_deliveries(self, date) -> list[Package]:
        """Returns the list of all scheduled deliveries on that date without mutating the _shipments or _shipments_list
        """
        delivery_list = []
        for item in self._shipment_list:
            if item[self.DATE] == date:
                tracking_number = item[self.NUM]
                package = self._shipments[tracking_number]
                delivery_list.append(package)

        return delivery_list

    def get_package(self, tracking_number: str) -> Package | str:
        """Returns the package based on the tracking number"""
        if tracking_number in self._shipments:
            return self._shipments[tracking_number]
        else:
            return "Package not found"
