#!/usr/bin/env python3
"""Create a sample four-hole mounting plate (all dimensions in mm)."""
import argparse
import json
from pathlib import Path
import cadquery as cq
import ezdxf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

W, H, T = 80.0, 50.0, 8.0
R = 3.0
HOLES = [(-30, -15), (30, -15), (-30, 15), (30, 15)]

def build(output: Path):
    output.mkdir(parents=True, exist_ok=True)
    part = cq.Workplane("XY").box(W,H,T).faces(">Z").workplane().pushPoints(HOLES).hole(2*R)
    cq.exporters.export(part, str(output/"plate.step"))
    cq.exporters.export(part, str(output/"plate.stl"))

    drawing = ezdxf.new("R2010")
    drawing.header["$INSUNITS"] = 4
    msp = drawing.modelspace()
    vertices = [(-W/2,-H/2),(W/2,-H/2),(W/2,H/2),(-W/2,H/2)]
    msp.add_lwpolyline(vertices, close=True)
    for x,y in HOLES: msp.add_circle((x,y), R)
    drawing.saveas(output/"plate_sketch.dxf")

    fig, ax = plt.subplots(figsize=(8,5))
    ax.add_patch(plt.Rectangle((-W/2,-H/2), W,H,fill=False,lw=2))
    for x,y in HOLES: ax.add_patch(plt.Circle((x,y), R,fill=False,lw=1.5))
    ax.set_aspect("equal")
    ax.set_xlim(-W/2-10,W/2+10)
    ax.set_ylim(-H/2-10,H/2+10)
    ax.set_xlabel("mm"); ax.set_ylabel("mm")
    ax.set_title("Demo: mounting plate top-view sketch")
    ax.grid(True,alpha=.25)
    fig.savefig(output/"plate_sketch.png",dpi=180,bbox_inches="tight")
    plt.close(fig)

    solid = part.val()
    manifest = {
        "purpose":"toolchain smoke test only; not an assignment answer",
        "units":"mm", "width":W, "height":H, "thickness":T,
        "hole_diameter":2*R, "hole_centers":HOLES,
        "solid_count":len(part.solids().vals()),
        "volume_mm3":round(solid.Volume(),3),
        "outputs":["plate.step","plate.stl","plate_sketch.dxf","plate_sketch.png"]
    }
    (output/"manifest.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
    return manifest

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",default="exports/demo")
    args=parser.parse_args()
    print(json.dumps(build(Path(args.out)),indent=2))
