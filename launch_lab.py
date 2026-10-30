"""Зручний ручний запуск Jupyter або Orange у підготовленому середовищі."""
import os
import sys
import tempfile
from pathlib import Path

root=Path(__file__).resolve().parent
os.chdir(root)
os.environ['PYTHONUTF8']='1'
os.environ['MPLCONFIGDIR']=str(root/'.mplconfig')
os.environ['IPYTHONDIR']=str(root/'.ipython')
os.environ['JUPYTER_CONFIG_DIR']=str(root/'.jupyter/config')
os.environ['JUPYTER_DATA_DIR']=str(root/'.jupyter/data')
# Кожен користувач створює власні службові файли. Файли, створені
# sandbox-користувачем під час перевірки, можуть бути недоступні йому на запис.
os.environ['JUPYTER_RUNTIME_DIR']=tempfile.mkdtemp(prefix='lr4-jupyter-runtime-')
os.environ['JUPYTER_PATH']=str(root/'.jupyter/share/jupyter')
if '--orange' in sys.argv:
    os.environ.pop('QT_QPA_PLATFORM',None)
    args=[sys.executable,'-m','Orange.canvas',str(root/'потік_orange.ows')]
else:
    args=[sys.executable,'-m','jupyterlab',str(root/'ЛР4_Лопатін_12.ipynb'),
          '--notebook-dir',str(root)]
os.execv(sys.executable,args)
