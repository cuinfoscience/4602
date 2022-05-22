try:
    import pandas as pd
    assert pd.__version__ == "1.3.2"
except ImportError as e:
    print("error loading {}".format(e))

try:
    import altair as alt
    assert alt.__version__ == "4.1.0"
except ImportError as e:
    print("error loading {}".format(e))

try:
    import jupyterlab
    assert jupyterlab.__version__ == "3.1.7"
except ImportError as e:
    print("error loading {}".format(e))

try:
    import scipy
    assert scipy.__version__ == "1.7.1"
except ImportError as e:
    print("error loading {}".format(e))

try:
    import sklearn
    assert sklearn.__version__ == "0.24.2"
except ImportError as e:
    print("error loading {}".format(e))


print("Your setup looks good!")
