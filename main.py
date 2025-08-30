import sys
from pathlib import Path

# blenderからプロジェクトのパスを認識できるようにする
project_path = Path(__file__).parent
project_path_str = project_path.__str__()

if not project_path_str in sys.path:
    sys.path.append(project_path_str)
    
