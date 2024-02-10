import os

tmp_dir = Path(os.environ['TEMP'])
if not tmp_dir.exists():
    tmp_dir = Path(os.environ['TMP'])
if not tmp_dir.exists():
    tmp_dir = Path()


