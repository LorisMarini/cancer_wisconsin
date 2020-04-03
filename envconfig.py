from dependencies import *

# Configure pandas behavior
warnings.filterwarnings('ignore')

# Make Jupyter Notebook cells larger
display(HTML("<style>.container { width:85% !important; }</style>"))

# Display all outputs when a cell has multiple variables
InteractiveShell.ast_node_interactivity = "all"

# Configure pandas behavior
pd.set_option('max_colwidth', 100)
pd.set_option("display.max_columns", 200)
pd.set_option("display.max_rows", 0)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# Configure matplotlib
matplotlib.rc_file("matplotlibrc")
