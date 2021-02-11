class EndpointConfig():
    """The configuration object used to create endpoints

    Attributes
    ----------
    name : str
        The name of the endpoint - not visible from outside
    route : str
        The endpoint route after the base url - e.g. /api/messages
    methods : list[str]
        The methods fro the endpoint, e.g. GET, POST, PUT, DELETE
    headers : dict
        The headers to return from the endpoint
    file_path : str
        The path to the return data of the endpoint
    """

    def __init__(self, name: str, route: str, methods: list[str],
                 headers: dict, file_path: str) -> None:
        self.name = name
        self.route = route
        self.methods = methods
        self.headers = headers
        self.file_path = file_path
