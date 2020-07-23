# Developer Installation

For a development installation, start by cloning the project from GitHub:

``` bash
$ git clone https://github.com/nicohlr/ipychart.git
```

Then, install nodejs:

``` bash
$ cd ipychart
$ conda install jupyterlab nodejs -c conda-forge
```

After that, you'll have to install the Javascript ipychart package ...

``` bash
# from the root of the project
$ cd ipychart/js
$ npm install 
```

... followed by the ipychart Python package:

``` bash
# from the root of the project
$ pip install -e .
```

Finally, install & enable the jupyter notebook extension:

``` bash
$ jupyter nbextension install --py --symlink --sys-prefix ipychart
$ jupyter nbextension enable --py --sys-prefix ipychart
```

You are now ready to develop ipychart !