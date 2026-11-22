import pathlib

TEXT = "Someone holds you the way they hold a full cup going down the stairs — not tight, just careful, eyes on the step, not on you. You don't have to be still. The tea doesn't spill. At the bottom they set you down slowly and you are still warm in their hands."

out_dir = pathlib.Path("/output")
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")
