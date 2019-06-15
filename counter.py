"""Character counter."""

import argparse


def count_char(value, limit=1000):
    # recursive case
    if len(value) > limit:
        count_char(value[:-limit], limit)

    # base case
    counts = {'a': 0, 'b': 0, 'c': 0}

    for key, val in counts.items():
        counts[key] = val + value.count(key)

    print(f"a:{counts['a']}, b:{counts['b']}, c:{counts['c']}\n")


if __name__ == '__main__':
    # Arg parser
    parser = argparse.ArgumentParser(description='Counter of some characters.')
    parser.add_argument(
        '--limit', metavar='limit',
        type=int, nargs=1, required=False,
        help='Limit of characters.', default=[1000]
    )
    args = parser.parse_args()
    limitation = args.limit[0]

    # Counter
    text = input('Enter text: ')
    count_char(text, limitation)
