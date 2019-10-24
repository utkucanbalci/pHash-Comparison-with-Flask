# pHash-Comparison-with-Flask
Better Error Handling will be provided.
This is an API for computing and comparing pHashes. Basic usage is provided in cli.py

/api/computeImage is for computing a pHash of an image by posting that image.

/api/computePath is for computing a pHash of an image by posting its filepath.(user and API should be running at the same machine or have access to the same folder)

/api/compareImages is for comparing images' pHashes by posting those images. Result is the calculated hamming distance between two images' pHashes.

/api/comparePaths is for comparing images by posting their filepaths. Result is the calculated hamming distance between two images' pHashes. (user and API should be running at the same machine or have access to the same folder)

Sample output of requests in cli.py:

{"pHash": "ada30ebac65b888d"}  

{"pHash": "a85ab7b553f00b4a"}

{"hamming_distance": "0", "pHash1": "ada30ebac65b888d", "pHash2": "ada30ebac65b888d"}

{"hamming_distance": "14", "pHash1": "a85ab7b553f00b4a", "pHash2": "ada30ebac65b888d"}

usage:

create your upload folder and state it in pHashAPI.py

After that, just run python3 pHashAPI.py for starting the API.
