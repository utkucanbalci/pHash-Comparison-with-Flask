# pHash-Comparison-with-Flask
Better Error Handling will be provided.
This is an API for computing and comparing pHashes. Basic usage is provided in cli.py

/api/computeImage is for computing a pHash of an image by posting that image.

/api/computePath is for computing a pHash of an image by sending its filepath.(user and API should be running at the same server)

/api/compareImages is for comparing images' pHashes by posting those images. Result is true if both are identical.

/api/comparePaths is for comparing images by posting their filepaths. Result is true if both are identical (user and API should be running at the same server)

Sample output for requests in cli.py:
{"pHash": "ada30ebac65b888d"}
{"pHash": "a85ab7b553f00b4a"}
{"pHash1": "ada30ebac65b888d", "pHash2": "a85ab7b553f00b4a", "result": "False"}
{"pHash1": "a85ab7b553f00b4a", "pHash2": "ada30ebac65b888d", "result": "False"}

usage:
just run python3 pHashAPI.py for starting the API.
