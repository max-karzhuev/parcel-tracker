"""Tests all of the functions and methods"""
from loco_date import LocoDate
from package import *
from tracker_functions import *
import pytest

"""LocoDate Tests:
________________________________________________________________________________________________________________________
"""


def test_get_date() -> None:
    """Test the get_date method"""
    ld1 = LocoDate(2007, 11, 3, "Vladivostok", "Russia")
    ld2 = LocoDate(2019, 10, 1, "Burlington", "Canada")
    assert ld1.get_date == date(2007, 11, 3)
    assert ld2.get_date == date(2019, 10, 1)



"""Package Tests:
________________________________________________________________________________________________________________________
"""


def test_set_departure() -> None:
    """Test the set_departure method"""
    package1 = Package("Max", "Sabrina", "TEST000001", "FedEx")
    package2 = Package("Hulk", "Spiderman", "TEST000002", "UPS")

    package1.set_departure(2026, 1, 3, "Toronto", "Canada")
    package2.set_departure(2000, 12, 28, "New York Ciity", "USA")

    assert package1._departure == LocoDate(2026, 1, 3, "Toronto", "Canada")
    assert package2._departure == LocoDate(2000, 12, 28, "New York Ciity", "USA")


def test_set_arrival() -> None:
    """Test the set_arrival method"""

    package1 = Package("Max", "Sabrina", "TEST000001", "FedEx")
    package2 = Package("Hulk", "Spiderman", "TEST000002", "UPS")

    package1.set_arrival(2026, 1, 3, "Toronto", "Canada")
    package2.set_arrival(2000, 12, 28, "New York Ciity", "USA")

    assert package1._arrival == LocoDate(2026, 1, 3, "Toronto", "Canada")
    assert package2._arrival == LocoDate(2000, 12, 28, "New York Ciity", "USA")


def test_set_departure_or_arrival_with_TypeError() -> None:
    """Test the set_departure and set_arrival methods with a TypeError arising"""

    package1 = Package("Max", "Sabrina", "TEST000001", "FedEx")
    package2 = Package("Hulk", "Spiderman", "TEST000002", "UPS")

    package1.set_departure(2025, 11, 12, "London", "UK")
    package2.set_departure(2000, 9, 4, "Pekin", "China")
    package1.set_arrival(2026, 1, 3, "Toronto", "Canada")
    package2.set_arrival(2000, 12, 28, "New York Ciity", "USA")

    assert package1._departure == LocoDate(2025, 11, 12, "London", "UK")
    assert package2._departure == LocoDate(2000, 9, 4, "Pekin", "China")
    assert package1._arrival == LocoDate(2026, 1, 3, "Toronto", "Canada")
    assert package2._arrival == LocoDate(2000, 12, 28, "New York Ciity", "USA")


def test_is_domestic() -> None:
    """Test the is_domestic method"""
    package1 = Package("Max", "Sabrina", "TEST000001", "FedEx")
    package2 = Package("Hulk", "Spiderman", "TEST000002", "UPS")

    package1.set_departure(2025, 11, 12, "London", "UK")
    package2.set_departure(2000, 9, 4, "Pekin", "China")
    package1.set_arrival(2026, 1, 3, "Toronto", "Canada")
    package2.set_arrival(2000, 12, 28, "Shanghai", "China")

    assert not package1.is_domestic()
    assert package2.is_domestic()


def test_domestic_without_locations() -> None:
    """Test checking domestic status without location"""
    package = Package("Maksim", "Sabrina", "TEST000001", "FedEx")
    with pytest.raises(IncompletePackageInfoError):
        package.is_domestic()


def test_transit_days_different_days() -> None:
    """Test the transit_days method with different days"""
    package = Package("Amazon", "Micheal Scott", "TEST000001", "Huiawei")

    package.set_departure(2003, 11, 3, "Moscow", "Russia")
    package.set_arrival(2003, 11, 15, "Barcelona", "Spain")

    assert package.transit_days() == 12


def test_transit_days_different_months() -> None:
    """Test the transit_days method with different months"""
    package = Package("Amazon", "Micheal Scott", "TEST000001", "Huiawei")

    package.set_departure(2003, 11, 3, "Moscow", "Russia")
    package.set_arrival(2003, 12, 14, "Barcelona", "Spain")

    assert package.transit_days() == 41


def test_transit_days_different_years() -> None:
    """Test the transit_days method with different years, no leap year"""
    package = Package("Amazon", "Micheal Scott", "TEST000001", "Huiawei")

    package.set_departure(2025, 8, 28, "Moscow", "Russia")
    package.set_arrival(2026, 8, 30, "Barcelona", "Spain")

    assert package.transit_days() == 367


def test_transit_days_leap_year() -> None:
    """Test the transit_days method with different years, with a leap year"""
    package = Package("Amazon", "Micheal Scott", "TEST000001", "Huiawei")

    package.set_departure(2024, 1, 28, "Moscow", "Russia")
    package.set_arrival(2026, 1, 30, "Barcelona", "Spain")

    assert package.transit_days() == 732


def test_transit_days_without_dates() -> None:
    """Test checking transit days without dates"""
    package = Package("Maksim", "Sabrina", "TEST000001", "FedEx")
    with pytest.raises(IncompletePackageInfoError):
        package.transit_days()



"""Letter [Package sub class] Tests:
------------------------------------------------------------------------------------------------------------------------
"""


def test_set_type() -> None:
    """Test the set_type method for a letter"""
    letter1 = Letter(2007, 3, 3, "Berlin", "Germany", 2008, 6, 7, "Rio", "Brazil", "John", "Leslie", "TEST000001",
                    "FedEx", 150, 150, 3, 4) #Standard
    letter2 = Letter(2007, 3, 3, "Berlin", "Germany", 2008, 6, 7, "Rio", "Brazil", "John", "Leslie", "TEST000002",
                        "FedEx", 260, 150, 3, 4) #Non-standard

    assert letter1.type == "standard"
    assert letter2.type == "non-standard"


def test_set_type_dimensions_correction() -> None:
    """Test the type of letter being set and then being modified"""
    letter1 = Letter(2007, 3, 3, "Berlin", "Germany", 2008, 6, 7, "Rio", "Brazil", "John", "Leslie", "TEST000001",
                        "FedEx", 150, 150, 3, 4) #Standard
    letter2 = Letter(2007, 3, 3, "Berlin", "Germany", 2008, 6, 7, "Rio", "Brazil", "John", "Leslie", "TEST000001",
                        "FedEx", 150, 150, 3, 4) #Standard
    letter3 = Letter(2007, 3, 3, "Berlin", "Germany", 2008, 6, 7, "Rio", "Brazil", "John", "Leslie", "TEST000001",
                        "FedEx", 150, 150, 3, 4) #Standard

    assert letter1.type == "standard"
    assert letter2.type == "standard"
    assert letter3.type == "standard"

    letter1.set_type(280, 95, 4, 12) #Standard
    letter2.set_type(360, 240, 20, 305) #Non-standard

    with pytest.raises(WrongPackageTypeError):
        letter3.set_type(670, 670, 670, 670) #Not a letter

    assert letter1.type == "standard"
    assert letter2.type == "non-standard"
    assert letter3.type == "not a letter"


def test_set_type_with_exception() -> None:
    """Test the initilizer on a "not a letter" type letter"""
    with pytest.raises(WrongPackageTypeError):
        letter = Letter(2026, 1, 23, "Madrid", "Spain", 2027, 12, 5, "St Petersburg", "Russia", "ChatGPT", "ClaudAI",
                    "TEST676941", "FEDEX", 1000, 30000, 500, 4000)



"""Parcel [Package sub class] Tests:
------------------------------------------------------------------------------------------------------------------------
"""


def test_set_size() -> None:
    """Test setting size on a parcel"""
    parcel = Parcel(2007, 7, 11, "Hamilton", "Canada", 2007, 11, 3, "Vladivostok", "Russia", "Sabrina", "Maksim",
                    "TEST000001", "Amamzon", 0, 0, 0, 0)

    parcel.set_size(300, 500, 46)

    assert parcel.size == (300, 500, 46)


def test_set_weight() -> None:
    """Test setting weight on a parcel"""
    parcel = Parcel(2007, 7, 11, "Hamilton", "Canada", 2007, 11, 3, "Vladivostok", "Russia", "Sabrina", "Maksim",
                    "TEST000001", "Amamzon", 0, 0, 0, 0)

    parcel.set_weight(3200)

    assert parcel.weight == 3200


def test_volume() -> None:
    """Test the volume calculator"""
    parcel1 = Parcel(2007, 7, 11, "Hamilton", "Canada", 2007, 11, 3, "Vladivostok", "Russia", "Sabrina", "Maksim",
                        "TEST000001", "Amamzon", 320, 500, 640, 0)
    parcel2 = Parcel(2007, 7, 11, "Hamilton", "Canada", 2007, 11, 3, "Vladivostok", "Russia", "Sabrina", "Maksim",
                        "TEST000002", "Amamzon", 430, 32, 400, 0)

    assert parcel1.volume() == 102400
    assert parcel2.volume() == 5504


def test_volume_with_exception() -> None:
    """Test the volume calculator with an exception"""
    with pytest.raises(IncompletePackageInfoError):
        parcel = Parcel(2007, 7, 11, "Hamilton", "Canada", 2007, 11, 3, "Vladivostok", "Russia", "Sabrina", "Maksim",
                            "TEST000001", "Amamzon", 0, 0, 0, 0)



"""ShipmentList Tests:
________________________________________________________________________________________________________________________
"""


def test_is_empty() -> None:
    """Tests the is_empty method"""
    lst1 = ShipmentList()
    lst2 = ShipmentList()

    parcel1 = Parcel(2007, 7, 11, "Hamilton", "Canada", 2007, 11, 3, "Vladivostok", "Russia", "Sabrina", "Maksim",
                            "TEST000001", "Amamzon", 320, 500, 640, 0)
    parcel2 = Parcel(2007, 7, 11, "Hamilton", "Canada", 2007, 11, 3, "Vladivostok", "Russia", "Sabrina", "Maksim",
                            "TEST000002", "Amamzon", 430, 32, 400, 0)

    lst2.enqueue(parcel1)
    lst2.enqueue(parcel2)

    assert lst1.is_empty is True
    assert lst2.is_empty is False


def test_intializes_empty() -> None:
    """Tests that the ShipmentList initiaalizes as zero"""
    lst = ShipmentList()
    assert lst.is_empty == True


def test_enqueue() -> None:
    """Tests the enqueue method"""
    lst = ShipmentList()
    parcel = Parcel(2007, 7, 11, "Hamilton", "Canada", 2007, 11, 3, "Vladivostok", "Russia", "Sabrina", "Maksim",
                                "TEST000001", "Amamzon", 320, 500, 640, 0)

    assert lst.is_empty is True
    lst.enqueue(parcel)
    assert lst.is_empty is False


def test_get_package_nonempty_list() -> None:
    """Test the get_package method on a non-empty list"""
    lst = ShipmentList()
    parcel1 = Parcel(2007, 7, 11, "Hamilton", "Canada", 2007, 11, 3, "Vladivostok", "Russia", "Sabrina", "Maksim",
                                "TEST000001", "Amamzon", 320, 500, 640, 0)
    parcel2 = Parcel(2007, 7, 11, "Hamilton", "Canada", 2007, 11, 3, "Vladivostok", "Russia", "Sabrina", "Maksim",
                                "TEST000002", "Amamzon", 430, 32, 400, 0)
    letter1 = Letter(2007, 3, 3, "Berlin", "Germany", 2008, 6, 7, "Rio", "Brazil", "John", "Leslie", "TEST000003",
                        "FedEx", 150, 150, 3, 4) #Standard
    letter2 = Letter(2007, 3, 3, "Berlin", "Germany", 2008, 6, 7, "Rio", "Brazil", "John", "Leslie", "TEST000004",
                            "FedEx", 260, 150, 3, 4) #Non-standard

    lst.enqueue(parcel1)
    lst.enqueue(parcel2)
    lst.enqueue(letter1)
    lst.enqueue(letter2)

    assert lst.get_package("TEST000001") == parcel1
    assert lst.get_package("TEST000002") == parcel2
    assert lst.get_package("TEST000003") == letter1
    assert lst.get_package("TEST000004") == letter2


def test_get_package_doesnt_mutate() -> None:
    """Test that the get_package method doesn't mutate the ShipmentList"""
    lst = ShipmentList()
    parcel1 = Parcel(2007, 7, 11, "Hamilton", "Canada", 2007, 11, 3, "Vladivostok", "Russia", "Sabrina", "Maksim",
                                "TEST000001", "Amamzon", 320, 500, 640, 0)
    parcel2 = Parcel(2007, 7, 11, "Hamilton", "Canada", 2007, 11, 3, "Vladivostok", "Russia", "Sabrina", "Maksim",
                                "TEST000002", "Amamzon", 430, 32, 400, 0)
    letter1 = Letter(2007, 3, 3, "Berlin", "Germany", 2008, 6, 7, "Rio", "Brazil", "John", "Leslie", "TEST000003",
                        "FedEx", 150, 150, 3, 4) #Standard
    letter2 = Letter(2007, 3, 3, "Berlin", "Germany", 2008, 6, 7, "Rio", "Brazil", "John", "Leslie", "TEST000004",
                            "FedEx", 260, 150, 3, 4) #Non-standard

    assert lst.active_shipments == 4

    lst.enqueue(parcel1)
    lst.enqueue(parcel2)
    lst.enqueue(letter1)
    lst.enqueue(letter2)

    lst.get_package("TEST000001")
    lst.get_package("TEST000002")
    lst.get_package("TEST000003")
    lst.get_package("TEST000004")

    assert lst.active_shipments == 4


def test_get_package_on_empty_list() -> None:
    """Tests the get_shipmnent method on an empty ShippingList"""
    lst = ShipmentList()

    assert lst.get_package("TEST000001") == "Package not found"


def test_deliver_orders() -> None:
    """Tests the deliver method on ShipmentList"""
    lst = ShipmentList()
    parcel1 = Parcel(2007, 7, 11, "Hamilton", "Canada", 2007, 11, 3, "Vladivostok", "Russia", "Sabrina", "Maksim",
                                    "TEST000001", "Amamzon", 320, 500, 640, 0)
    parcel2 = Parcel(2007, 7, 11, "Hamilton", "Canada", 2007, 11, 3, "Vladivostok", "Russia", "Sabrina", "Maksim",
                                    "TEST000002", "Amamzon", 430, 32, 400, 0)
    letter1 = Letter(2007, 3, 3, "Berlin", "Germany", 2008, 6, 7, "Rio", "Brazil", "John", "Leslie", "TEST000003",
                            "FedEx", 150, 150, 3, 4) #Standard
    letter2 = Letter(2007, 3, 3, "Berlin", "Germany", 2008, 6, 7, "Rio", "Brazil", "John", "Leslie", "TEST000004",
                                "FedEx", 260, 150, 3, 4) #Non-standard
    deliverydate = date(2007, 11, 3)

    lst.enqueue(parcel1)
    lst.enqueue(parcel2)
    lst.enqueue(letter1)
    lst.enqueue(letter2)

    assert lst.active_shipments == 4

    assert lst.deliver(deliverydate) == [parcel1, parcel2]
    assert lst.active_shipments == 2


def test_check_scheduled_deliveries() -> None:
    """Tests the check_scheduled_deliveries method on ShipmentList"""
    lst = ShipmentList()
    parcel1 = Parcel(2007, 7, 11, "Hamilton", "Canada", 2007, 11, 3, "Vladivostok", "Russia", "Sabrina", "Maksim",
                                    "TEST000001", "Amamzon", 320, 500, 640, 0)
    parcel2 = Parcel(2007, 7, 11, "Hamilton", "Canada", 2007, 11, 3, "Vladivostok", "Russia", "Sabrina", "Maksim",
                                    "TEST000002", "Amamzon", 430, 32, 400, 0)
    letter1 = Letter(2007, 3, 3, "Berlin", "Germany", 2008, 6, 7, "Rio", "Brazil", "John", "Leslie", "TEST000003",
                            "FedEx", 150, 150, 3, 4) #Standard
    letter2 = Letter(2007, 3, 3, "Berlin", "Germany", 2008, 6, 7, "Rio", "Brazil", "John", "Leslie", "TEST000004",
                                "FedEx", 260, 150, 3, 4) #Non-standard
    deliverydate = date(2007, 11, 3)

    lst.enqueue(parcel1)
    lst.enqueue(parcel2)
    lst.enqueue(letter1)
    lst.enqueue(letter2)

    assert lst.active_shipments == 4

    assert lst.check_scheduled_deliveries(deliverydate) == [parcel1, parcel2]
    assert lst.active_shipments == 4



"""Tracker_functions Tests:
________________________________________________________________________________________________________________________
"""


def test_check_borders_letters() -> None:
    """Test check_borders on a Letter type"""
    letter1 = Letter(2007, 3, 3, "Berlin", "Germany", 2008, 6, 7, "SomeOtherGermanCity", "Germany", "John", "Leslie",
                     "TEST000003", "FedEx", 150, 150, 3, 4) #Standard
    letter2 = Letter(2007, 3, 3, "Berlin", "Germany", 2008, 6, 7, "Rio", "Brazil", "John", "Leslie", "TEST000004",
                                    "FedEx", 260, 150, 3, 4) #Non-standard

    assert check_borders(letter1) == "Domestic"
    assert check_borders(letter2) == "International"

#def test_check_borders_parcels() -> None:
