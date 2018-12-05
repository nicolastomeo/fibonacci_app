from flask import abort, request, jsonify
from fibonacci import cache
from fibonacci.fib import fib
from fibonacci.fib.fibonacci_calc import fibonacci_generator, fibonacci_generator_cache, CacheCorrupted


@fib.route('/<int:start_index>/<int:end_index>')
def fibonacci_sequence(start_index, end_index):
    """
    Endpoint where the Fibonacci Sequence from start_index to end_index is calculated.
    Url param nocache=1 calculates the sequence without cache.

    :param start_index: Index from where the Fibonacci Sequence starts
    :param end_index:  Index where the Fibonacci Sequence ends.
    :return: Json list of Fibonacci Sequence
    """
    if start_index < 0 or end_index < 0:
        abort(400, "start_index and end_index must be positive")
    elif end_index < start_index:
        abort(400, "end_index can't be bigger than start_index")
    if request.args.get('nocache', None):
        fib_seq = list(fibonacci_generator(start_index, end_index))
    else:
        try:
            fib_seq = list(fibonacci_generator_cache(start_index, end_index, cache))
        except CacheCorrupted:
            cache.clear() #cache is cleared in case of corruption
            fib_seq = list(fibonacci_generator_cache(start_index, end_index, cache))

    return jsonify(fib_seq)
