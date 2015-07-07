## Overview
This is a simple python script that generates an image given binary data from any file. It doesn't matter what type of file, it's meant to explore internal file organization and structure by visualizing it as a bitmap.

### Why?
This was inspired by the TED talk ["The 1s and 0s behind cyber warfare"](https://www.ted.com/talks/chris_domas_the_1s_and_0s_behind_cyber_warfare?language=en)

Also, because python can do anything! I know there are other tools out there that do something similar, but I didn't find one written in python and I thought it would be a great exercise with which to learn a little numpy and image manipulation.

## Usage
**Python 3** is required.

```
    visualize.py <filename> [--mmap | --np-memmap | --np-fullcolor]

Options:
    --np-fullcolor  Use numpy to extract data in 4-byte chunks and draw in full color
    --np-memmap     Use numpy but run it with .memmap instead of .fromfile
    --mmap          Use mmap and regular file i/o instead of numpy fromfile.
    --version       Show version.
    -h --help       Show this screen.
```

## Under the covers
The default mode for reading data is through the use of numpy .fromfile to load it into memory and generate the image pixels. As you can see from the command line options, I'm experimenting with different modes trying to learn a bit about what could be more performant.

If you find any problems or have a suggestion, feel free to drop an issue I can look at or send a message to [@tryexceptpass](http://www.twitter.com/tryexceptpass).