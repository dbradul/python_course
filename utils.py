
def parse_length(request, default=10):
    value = request.args.get('length', str(default))

    if not value.isnumeric():
        raise ValueError('Not a number')

    value = int(value)
    if not 3 < value < 100:
        raise ValueError('Out of range')

    return value
