from loco_date import LocoDate
from package import *
from tracker_functions import *


if __name__ == "__main__":

    filename = "/Users/mk/Documents/Codex/2026-09-27/th/outputs/parcel-tracker/sample_packages.csv"

    sl = ShipmentList()

    load_shipping_list(filename, sl)
    package = sl.get_package("DEMO00000004")
    # print(package)
    # if isinstance(package, Package):
    #     print(check_borders(package))

    date = date(2026, 10, 7)
    for p in sl.deliver(date):
        print(p)
