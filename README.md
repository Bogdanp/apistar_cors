# apistar-cors

CORS support for [API Star].


## Installation

    pipenv install apistar_cors


## Usage

``` python
from apistar import App
from apistar_cors import CORSMixin


class App(CORSMixin, WSGIApp):
  pass


COMPONENTS = [
    # ...
]

ROUTES = [
    # ...
]

app = App(
    components=COMPONENTS,
    routes=ROUTES,
)
```


## License

apistar_cors is licensed under Apache 2.0.  Please see [LICENSE]
for licensing details.


[API Star]: https://github.com/encode/apistar/
[LICENSE]: https://github.com/Bogdanp/apistar_cors/blob/master/LICENSE
