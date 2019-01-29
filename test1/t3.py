from functools import partial


def request_preprocessor(prepped_req, *args, **kwargs):
    raise NotImplementedError


request_preprocessor = partial(request_preprocessor)
print(request_preprocessor)