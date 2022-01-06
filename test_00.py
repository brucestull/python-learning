def print_movie_ratings(username, *args, **kwargs):
    """Update the user’s ratings for movies.
    Update movies from *args that are keys in **kwargs.
    """

    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    # print(args)
    # print(kwargs)

    for arg in args:  # Loop through the tuple `args`
        if arg in kwargs:  # Loop through keys of the `kwargs` dictionary
            print(arg, kwargs[arg])

print_movie_ratings('jane', 'Sharknado', 'Frozen', 'Transformers', Sharknado=3, Frozen=2, Fargo=5)

""" Output is:
Sharknado 3
Frozen 2
"""