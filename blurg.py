import Image
import ImageFilter
import argparse
import os
import re
import sys

__version__ = '0.2.2'

debug = False
silent = False
dry_run = False
 
class GaussianBlur(ImageFilter.Filter):
    """
    compensate for a bug in PIL 1.1.7
    """
    name = "GaussianBlur"

    def __init__(self, radius=2):
        self.radius = radius
    def filter(self, image):
        return image.gaussian_blur(self.radius)

def console_out(format_str, *args, **kwargs):
    if not silent:
        print format_str.format(*args, **kwargs)

def console_debug(format_str, *args, **kwargs):
    if debug and not silent:
        sys.stderr.write(format_str.format(*args, **kwargs))
        sys.stderr.write(os.linesep)

def gblur(in_image, out_image, radius):
    if dry_run:
        console_out("    DRY RUN - gblur in_image: {}, out_image: {}", in_image, out_image)
        return

    im = Image.open(in_image)
    console_debug("    ...image format: {}, size: {}, mode: {}", im.format, im.size, im.mode)
     
    # apply BLUR filter
    # gb = ImageFilter.GaussianBlur(45)
    gb = GaussianBlur(radius)
    im_blur = im.filter(gb)
    #im_blur = gb.filter(Im)
    #Im_blur = Im.GaussianBlur(35)
    #Im_blur = Im.filter(ImageFilter.BLUR)
    im_blur.save(out_image)
    console_out("    ...image saved!", im.format, im.size, im.mode)

def normalize_dir(d):
    '''
    get rid of things like ~/ and ./ on a directory

    d -- string
    return -- string -- d, now with 100% more absolute path
    '''
    d = os.path.expanduser(d)
    d = os.path.abspath(d)
    return d


def console():
    # http://docs.python.org/library/argparse.html#module-argparse
    parser = argparse.ArgumentParser(description='Take an in-dir, blur the images and put them in out-dir')
    parser.add_argument("-i", "--in-dir", dest="in_dirs", action='append', default=[], help="the directory to read images from")
    parser.add_argument("-o", "--out-dir", dest="out_dir", default=u"", help="the directory to save images to")
    parser.add_argument("--dry-run", dest="dry_run", action='store_true', help="dry run, don't actually do anything")
    parser.add_argument("--version", action='version', version="%(prog)s {}".format(__version__))
    parser.add_argument("--silent", dest="silent", action='store_true', help="no output")
    parser.add_argument("--debug", dest="debug", action='store_true', help="turn on more verbose output")
    parser.add_argument("-r", "--radius", dest="radius", default=50, type=int, help="how blurry you want the images")

    args = parser.parse_args()

    global debug
    global silent
    global dry_run
    debug = args.debug
    silent = args.silent
    dry_run = args.dry_run

    regex = re.compile(ur'\.(?:jpe?g|gif|png)$', re.I)

    out_dir = normalize_dir(args.out_dir)
    if not os.path.isdir(out_dir):
        console_out("creating OUT dir: {}", out_dir)
        os.makedirs(out_dir)

    console_out("placing images in OUT dir: {}", out_dir)
    
    for in_dir in args.in_dirs:
        in_dir = normalize_dir(in_dir)

        console_out("checking IN dir: {}", in_dir)
        if os.path.isdir(in_dir):
            for root, dirs, files in os.walk(in_dir, topdown=True):
                dirs[:] = [d for d in dirs if d[0] != '.'] # ignore dot directories
                for f in files:
                    if regex.search(f):
                        in_filepath = os.path.join(root, f)
                        out_filename = "gblur-{}-{}".format(args.radius, f)
                        out_filepath = os.path.join(out_dir, out_filename)
                        if os.path.isfile(out_filepath):
                            console_out("    ...image {} exists in OUT dir, moving on", out_filename)
                        else:
                            console_out("    ...Gaussian bluring image {} -> {}", f, out_filename)
                            gblur(in_filepath, out_filepath, args.radius)

                    else:
                        console_debug("    ...ignoring {}, not an image", f)

        else:
            console_out("    ...not a valid directory, ignoring")

if __name__ == "__main__":
    sys.exit(console())

