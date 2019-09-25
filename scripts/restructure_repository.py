#! /usr/bin/env python

from pprint import pprint as pp
import csv
import os


csvfiles = {
    directory: csvfiles
    for (directory, _, files) in os.walk(".")
    if ".git" not in directory
    for csvfiles in [[f for f in files if f[-4:] == ".csv"]]
    if csvfiles
}


def transpose(l):
    assert all([len(l[i]) == len(l[i + 1]) for i in range(len(l) - 1)]), (
        "Trying to transpose a list of lists where the nested lists have "
        "differing lengths."
    )
    return list(map(list, zip(*l)))


def consolidate(directory, files):
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
            if f in files:
                files.remove(f)
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


def canonicalize(directory, files):
    canon = {
        "Curtailment": "Curtailment",
        "Gas": "Gas",
        "PV": "Photovoltaics",
        "PHS1": "Pumped Hydro Storage 1",
        "PHS2": "Pumped Hydro Storage 2",
        "el": "Electricity",
        "co2": "CO_2",
    }
    canon = {
        "PHS": canon["PHS1"],
        "Gas plant": canon["Gas"],
        "Photovoltaics": canon["PV"],
        "pv": canon["PV"],
        "gas": canon["Gas"],
        "pmp_hydro": canon["PHS"],
        "pmp_hydro2": canon["PHS2"],
        "photovoltaics": canon["PV"],
        "phs": canon["PHS1"],
        "CO2": canon["co2"],
        "elec": canon["el"],
        "Elec": canon["el"],
    }


if __name__ == "__main__":
    for directory in csvfiles:
        consolidate(directory, csvfiles[directory])
