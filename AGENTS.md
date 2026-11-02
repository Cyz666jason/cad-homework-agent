# Instructions for CAD Codex agent

- Treat uploaded drawings as the authoritative source; never invent dimensions or geometric constraints.
- For each assignment, record a dimension table with source-view references and highlight unknowns.
- Work in millimeters unless the original task specifies otherwise.
- Build a deterministic parameterized Python script for each model using CadQuery and ezdxf.
- Preserve the actual assignment geometry: the demo plate is ONLY an environment test.
- Export required formats; use STEP/STL for 3D, DXF/PNG for 2D when permitted.
- Validate bounding dimensions, hole count, center positions, solid count and volumes if meaningful.
- Use 'bash scripts/smoke_test.sh' for environment validation. Report failures rather than claiming success.
- SolidWorks native SLDPRT and editable FreeCAD FCStd files require their respective applications; do not rename STEP as native CAD.
- Save assignment deliverables separately under exports/assignment-sketch and exports/assignment-part.
- Explain all modifications and evidence of verification in Chinese.
- Never commit confidential source drawings or personal information to this public repository without explicit permission.
