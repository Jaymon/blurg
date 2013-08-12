# Blurg

A small command line script to take images from one directory, blur them, and put them in another directory.

I like blurry desktop backgrounds, not sure why, but I do, but I found opening a program like photoshop and blurring them myself took way too long, so I never had the amount of blurred background images I craved, this script solves that problem, which, admittedly, might be specific only to me.

## Installation

You have to have PIL installed.

You can grab pre-compiled PIL binaries for Windows [here](http://www.pythonware.com/products/pil/#pil117).

I think every other system can probably install PIL using pip:

    pip install PIL

Then you can install blurg using pip:

    pip install git+https://github.com/Jaymon/blurg#egg=blurg

## Use

You use Blurg via the command line, to see all the arguments you can pass in:

    blurg --help

As an example, here is how I would call it:

    $ blurg --in-dir "/path/to/Dropbox/Wallpaper/unprocessed" --out-dir "/path/to/Dropbox/Wallpaper/processed"

You can tweak the blur amount if you don't like the default radius of 50.

# License

Public Domain
