#!/usr/bin/env python3

import os
import re
import csv

file_dir = os.environ.get("SESSILE_DIR") or os.getcwd()

def drill_points(min_hole=2):
    # Define the regular expressions
    regex_tools = re.compile(r"^(T\d+)C(\d+.?\d*)$") # T1C1.0
    regex_drills_by_size = re.compile(r"T\d+(\nX-?\d+.\d+Y-?\d+.\d+)+") # T1\nX-1.0Y-1.0\nX1.0Y1.0
    regex_point= re.compile(r"^X(-?\d+.\d+)Y(-?\d+.\d+)") # X-1.0Y-1.0

    # Yay, context managers!
    with open(f"{file_dir}/case/combined_drill.drl", 'r') as file:
        drill_text = file.read()

    # Get the list of tools, enlarge small holes, and initialize drills_by_size
    tools = [(str(m.group(1)), float(m.group(2)) if float(m.group(2)) > min_hole else min_hole) for l in drill_text.split('\n') for m in [regex_tools.search(l)] if m]
    drills_by_size = { size: [] for tool, size in tools }
    
    # Extract the drill points by size
    for match in regex_drills_by_size.finditer(drill_text):
        lines = match.group().strip().split('\n')
        tool = lines[0]
        points = [(float(m.group(1)), float(m.group(2))) for line in lines[1:] for m in [regex_point.search(line)] if m ]   
        size = next(size for t, size in tools if t == tool)
        drills_by_size[size].extend(points)
    
    # Remove unused sizes and deduplicate the points
    return { size: list(set(points)) for size, points in drills_by_size.items() if points }

# print(drill_points())

def locations(ref=None):
    with open(f"{file_dir}/board/output/pcbs/jlcpcb/production_files/CPL-sessile.csv") as file:
        reader = csv.DictReader(file)
        locations = dict([(x['Designator'],x) for x in reader])
        return locations[ref] if ref else locations

# print(locations("SW1"))


