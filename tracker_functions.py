from loco_date import LocoDate
from python_ta.contracts import check_contracts
import csv

from package import *

def check_borders(package: Package) -> str:
    """Returns "International" or "Domestic" for the status of the package"""
    if package.is_domestic():
        return "Domestic"
    else:
        return "International"

def load_shipping_list(filename: str, sl: ShipmentList) -> ShipmentList:
    """Reurns the shipping list loaded from a cvs file. The function accepts a preloaded list and can modify it to add
    more shipments
    Preconitions:
    -filename is defined"""

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)


        for row in reader:
            dy = int(row["dyear"])
            dm = int(row["dmonth"])
            dd = int(row["dday"])
            dci = str(row["dcity"])
            dco = str(row["dcountry"])
            ay = int(row["ayear"])
            am = int(row["amonth"])
            ad = int(row["aday"])
            aci = str(row["acity"])
            aco = str(row["acountry"])
            sender = str(row["sender"])
            recipient = str(row["recipient"])
            tracking_number = str(row["tracking_number"])
            carrier = str(row["carrier"])
            l = int(row["length_mm"])
            w = int(row["width_mm"])
            t = int(row["thickness_mm"] or 0)
            h = int(row["height_mm"] or 0)
            weight = int(row["weight_g"])

            if row["package_kind"] == "Letter":
                if t == 0 and h > 0:
                    t, h = h, t
            elif h == 0 and t > 0:
                t, h = h, t

            if str(row["package_kind"]) == "Letter":
                try:
                    package = Letter(dy, dm, dd, dci, dco, ay, am, ad, aci, aco, sender, recipient, tracking_number,
                                    carrier, l, w, h or t, weight)

                except WrongPackageTypeError:
                    package = Parcel(dy, dm, dd, dci, dco, ay, am, ad, aci, aco, sender, recipient, tracking_number,
                                carrier, h, w, l, weight)

                except IncompletePackageInfoError:
                    continue

            else:
                package = Parcel(dy, dm, dd, dci, dco, ay, am, ad, aci, aco, sender, recipient, tracking_number,
                            carrier, h, w, l, weight)

            sl.enqueue(package)

    return sl
