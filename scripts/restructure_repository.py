#! /usr/bin/env python

from pprint import pprint as pp
import csv
import os


csvfiles = {
    directory: csvfiles
    for (directory, _, files) in os.walk(".")
    for csvfiles in [[f for f in files if f[-4:] == ".csv"]]
    if csvfiles
    if directory[:3] != "./."
}

for directory in csvfiles:
    with open(os.path.join(directory, "scalars.csv"), "w", newline="") as csvf:
        csvw = csv.writer(csvf)
        csvw.writerow(["Name", "Value"])
        for f in [
            "constraints.csv",
            "memory.csv",
            "objective.csv",
            "timebuild.csv",
            "variables.csv",
        ]:
            if f in csvfiles[directory]:
                csvfiles[directory].remove(f)
                path = os.path.join(directory, f)
                rows = list(
                    csv.reader(open(path, "r"), quoting=csv.QUOTE_NONE)
                )
                msg = "Scalar file '{}' contains more than one, i.e. {}, rows:"
                assert len(rows) <= 1, msg.format(path, len(rows))
                row = rows[0] if rows else []
                # This is needed because "urbs" has rows like this:
                #       Objective value,EURO,29613076962.079998
                if "objective.csv" == f:
                    row = row[-1:]
                csvw.writerow(
                    [f[:-4]] + [c.replace('"', "").strip() for c in row]
                )
                os.remove(path)

