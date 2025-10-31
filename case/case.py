#!/usr/bin/env python3

# This vpype command was necessary to get build123d to work with the svg
# It's now reimported to KiCad, so the KiBot exported version will work without processing 
# and be at least somewhat aligned with the drill file.
# vpype read default/sessile-Edge_Cuts_LEFT.svg linemerge --tolerance 3mm linesort reloop linesimplify write default/sessile-Edge_Cuts_LEFT_vpype.svg

# The origin shifts need to be resolved. I'm not sure how to get 
# KiCad/KiBot to export the svg and drill files with the same origin, but it is
# offset by exactly 210mm, which also happens to be the height of the sheet in KiCad...

# The build123d example 'Offset Part to Create Thin Features' 
# https://build123d.readthedocs.io/en/latest/introductory_examples.html#offset-part-to-create-thin-features
# seemed relevant, but I couldn't get it to work, so I had to boolean the void.

from holes import drill_points, locations
from build123d import *
# from ocp_vscode import show_object as show

# set_port(3939)

min_hole = 2
ps_height = 1.4 * MM
# pcb_thickness = 1.6 * MM
# hole_depth = 1.5 * MM

# Make the void space
with BuildPart() as pcb_void:
    with BuildSketch(Plane.XY
                     .shift_origin((67, -186.2, 0) * MM)) as edge_cuts:
        with BuildLine() as line:
            add(import_svg("case/sessile-brd-vpype.svg"))
        make_face()
    extrude(amount = 3 * MM)

# Build the power switch hole
with BuildPart() as ps_void:
    ps = locations('SW1')
    with Locations(Plane.XY
                   .offset(ps_height / 2)
                   .shift_origin((ps['Mid X'], ps['Mid Y'], ps_height / 2) * MM)) as locations:
        Box(length=4 * MM, width=15 * MM, height=ps_height)
    fillet(ps_void.edges(), radius=0.5 * MM)

# Make the case
with BuildPart() as case:
    with BuildSketch(Plane.XY
                     .offset(-1 * MM)
                     .shift_origin((67, -186.2, -1) * MM)) as outline:
        add(edge_cuts)
        offset(amount=2 * MM, min_edge_length=5 * MM) 
    extrude(amount=4 * MM)
    # Cut the pcb and power switch holes
    add(pcb_void, mode=Mode.SUBTRACT)
    add(ps_void, mode=Mode.SUBTRACT)

    # Drill thru holes
    # CounterSinkHoles seemed like the right choice, but the pcb didn't sit as neatly in them
    
    with Locations(Plane.XY):
        for tool, points in drill_points(min_hole).items():
            radius = (tool / 2) + 0.5 * MM 
            # counter_sink_radius = radius + 0.5  
            with Locations(points):
                Hole(radius)
                # CounterSinkHole(radius, counter_sink_radius, depth=hole_depth)

    # @todo get fillets working
    # top_face = case.faces().sort_by(Axis.Z)[-1]
    # fillet(top_face.edges(), radius=0.5 * MM)

# show(case)
export_step(case.part, file_path="case/case.step")
# export_stl(case.part, file_path="case.stl")
# export_stl(case.part, file_path="case_ascii.stl", ascii_format=True)
