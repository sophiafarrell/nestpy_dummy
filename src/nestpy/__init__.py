__version__ = '1.1.3'
__nest_version__ = '2.0.1'

from .nestpy import *

def _automatic_plots():
  """Make automatic plots for website
  
  Note that this imports matplotlib and os itself as
  this routine is only mean to be run by the test server.
  """
  plots_directory_name = 'nestpy_plots'
  _make_plots(plots_directory_name)

  # paramiko copy out
  
  
  
def _make_plots(plots_directory_name) 
  import matplotlib.pyplot as plt
  import os
  
  if os.path.isdir(plots_directory_name):
    raise RunTimeError("Directory %s exists" % plots_directory_name)
  os.mkdir('nestpy_plots')
  
  for plot_to_make in ['er.png', 'nr.png']:
    filename = os.path.join(plots_directory_name,
                            plot_to_make)
    plt.savefig(filename)
  
  
