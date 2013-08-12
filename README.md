# Blurg

A small command line script to take images from one directory, blur them, and put them in another directory.

I like blurry desktop backgrounds, not sure why, but I do, but opening a program like photoshop and blurring them myself took too long, so I never had the amount of blurred background images I wanted, this script solves that problem, which, admittedly, might solve a problem specific only to me.

## Installation

You have to have PIL installed.

You can pre-compiled PIL binaries for Windows [here](http://www.pythonware.com/products/pil/#pil117).

I think every other system can probably install PIL using pip:

    pip install PIL

Then you can install blurg using pip:

    pip install git+https://github.com/Jaymon/blurg#egg=blurg

## Use

You use Blurg via the command line, to see all the arguments you can pass in:

    blurg --help

As an example, here is how I would call it:

    $ blurg --in-dir "/path/to/Dropbox/Wallpaper/unprocessed" --out-dir "/path/to/Dropbox/Wallpaper/processed"

# License

Public Domain
