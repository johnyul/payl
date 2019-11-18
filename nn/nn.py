import arrow
import clipboard

start = '2014-03-28'

def nn_output(start,end):
    _start = arrow.get(start, tzinfo='+0800')
    _end = arrow.get(end, tzinfo='+0800')
    return (_end - _start).days

def combine_str(days):
    return 'NN-{:0>6d}'.format(days)

def main():
    now = arrow.now().floor('day')
    end = now
    r = combine_str(nn_output(start,end))
    clipboard.copy(r)
    text = clipboard.paste()
    print(text)


if __name__ == "__main__":
    main()
