#! /usr/bin/env python

from pprint import pprint as pp
import csv
import itertools as itt
import math
import os

import pandas as pd


csvfiles = {
    directory: csvfiles
    for (directory, _, files) in os.walk(".")
    if ".git" not in directory
    for csvfiles in [[f for f in files if f[-4:] == ".csv"]]
    if csvfiles
}


"""
def csvfiles(root):
    return {
        directory: csvfiles
        for (directory, _, files) in os.walk(root)
        if ".git" not in directory
        for csvfiles in [[f for f in files if f[-4:] == ".csv"]]
        if csvfiles
    }
"""


def transpose(l):
    assert all([len(l[i]) == len(l[i + 1]) for i in range(len(l) - 1)]), (
        "\nTrying to transpose a list of lists where the nested lists have "
        "differing lengths:\n{}".format([len(x) for x in l])
    )
    return list(map(list, zip(*l)))


def consolidate(directory, files):
    with open(os.path.join(directory, "scalars.csv"), "x", newline="") as csvf:
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
                    [f[:-4]] + [float(c.replace('"', "").strip()) for c in row]
                )
                os.remove(path)


def canonicalize(string, log=None):
    """ Transforms `string` into a canonical form.
    """
    canon = {
        "Curtailment": "Curtailment",
        "Gas": "Gas",
        "PV": "Photovoltaics",
        "PHS1": "Pumped Hydro Storage 1",
        "PHS2": "Pumped Hydro Storage 2",
        "el": "Electricity",
        "co2": "CO_2",
        "TS": "Timestamp",
    }
    canon_updates = {
        "PHS": canon["PHS1"],
        "Gas plant": canon["Gas"],
        "Photovoltaics": canon["PV"],
        "pv": canon["PV"],
        "gas": canon["Gas"],
        "pmp_hydro": canon["PHS1"],
        "pmp_hydro2": canon["PHS2"],
        "photovoltaics": canon["PV"],
        "phs": canon["PHS1"],
        "CO2": canon["co2"],
        "elec": canon["el"],
        "Elec": canon["el"],
        "Timestep": "",
        "sit": "",
        "Production per timestep [MWh]": "",
        "stf": "",
        "t": "",
        "Year": "",
        "Time": "",
        "timeindex": "",
    }
    canon.update(canon_updates)
    mangled = string.replace('"', "").strip()
    result = canon[mangled] if mangled in canon else mangled
    if log is not None and string != result:
        log.write("Replaced '{}' with '{}'\n".format(string, result))
    return result


def empty(path):
    """ Checks whether a file is "empty", i.e. contains only whitespace.
    """
    with open(path, "r") as f:
        return not bool("".join([l.strip() for l in f.readlines()]))


def split_csv(directory, name):
    """ Splits the provided CSV file into well formatted CSV files.
    """
    name = name[:-4]  # Removes ".csv" suffix
    components = [canonicalize(s) for s in name.split("_")]
    if len(components) == 1:
        components.append(canonicalize("el"))
    with open(os.path.join(directory, name + ".csv"), "r") as f:
        rows = [
            x
            for l in csv.reader(f, quoting=csv.QUOTE_NONE)
            for x in ([canonicalize(s) for s in l],)
            if any(x)
        ]
        columns = {
            key: list(group)
            for key, group in itt.groupby(transpose(rows), key=lambda l: l[0])
        }
        timestamps = (
            [
                str(
                    pd.Timestamp(year)
                    + pd.Timedelta("{}H".format(math.floor(float(hour)) - 1))
                )
                for year, hour in list(zip(*columns[""]))[2:]
            ]
            if len(columns[""]) == 2
            else [
                (
                    s
                    if not pd.isna(pd.to_datetime(s, errors="coerce"))
                    else str(
                        pd.Timestamp("2015")
                        + pd.Timedelta("{}H".format(math.floor(float(s)) - 1))
                    )
                )
                for s in columns[""][0][2:]
            ]
        )
        assert timestamps, "No timestamps?\nGot: {}".format(timestamps)
        timestamps = [canonicalize("TS")] + timestamps
        for header in [key for key in columns if key]:
            with open(
                os.path.join(
                    directory,
                    ".".join(components + [canonicalize(header)]) + ".csv",
                ),
                "x",
            ) as target:
                csv.writer(
                    target,
                    delimiter=",",
                    quotechar='"',
                    quoting=csv.QUOTE_MINIMAL,
                ).writerows(
                    transpose(
                        [timestamps]
                        + [column[1:] for column in columns[header]]
                    )
                )


if __name__ == "__main__":
    for directory in csvfiles:
        if "scalars.csv" in csvfiles[directory]:
            csvfiles[directory].remove("scalars.csv")
        else:
            consolidate(directory, csvfiles[directory])
        for name in csvfiles[directory]:
            if empty(os.path.join(directory, name)):
                csvfiles[directory].remove(name)
                continue
            split_csv(directory, name)
