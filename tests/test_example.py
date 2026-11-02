import json
import math
from pathlib import Path
import cadquery as cq
import ezdxf
from scripts.build_example import build

def test_demo(tmp_path: Path):
    info=build(tmp_path)
    for f in info["outputs"]:
        assert (tmp_path/f).is_file()
        assert (tmp_path/f).stat().st_size > 100
    assert info["solid_count"] == 1
    expected=80*50*8-4*math.pi*3**2*8
    assert math.isclose(info["volume_mm3"],expected,abs_tol=0.02)
    drawing=ezdxf.readfile(tmp_path/"plate_sketch.dxf")
    assert len(list(drawing.modelspace().query("CIRCLE"))) == 4
    solid=cq.importers.importStep(str(tmp_path/"plate.step"))
    assert len(solid.solids().vals()) == 1
    assert json.loads((tmp_path/"manifest.json").read_text())["units"] == "mm"
