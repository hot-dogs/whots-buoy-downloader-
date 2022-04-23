#!/usr/bin/env python3
import argparse
import roman
import sys
from urllib.request import urlopen


def parse_args():
    """
      Parse input arguments
    """
    parser = argparse.ArgumentParser(
        description="""WHOTS FILE DOWNLOADER 
        Example: If you want to download the raw system 1 from WHOTS 17, type:
        
        python3 whots_download_parser.py -w 17 -s 1""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "-w",
        type=int,
        nargs=1,
        dest="whots_number",
        help="Type the WHOTS buoy NUMBER (eg. `17` for WHOTS-17)",
        action="store"
    )

    parser.add_argument(
        "-s",
        type=int,
        nargs=1,
        dest="system_number",
        help="WHOTS SYSTEM NUMBER: ( 1 or 2 )",
        action="store"
    )

    if len(sys.argv) <= 4:
        parser.print_help()
        sys.exit()
    else:
        args = parser.parse_args()

    return args


class WhotsFileDownloader:
    """WHOTS File Downloader class.

    WHOTS file downloader are the ones responsible for downloading the WHOTS text files and writing it to disk.
    """

    def __init__(self, whots_number, system_number):
        self.whots_number = whots_number
        self.system_number = system_number
        self.content = None
        self.read_file = None

    def get_whots_system(self):
        self.content = "https://uop.whoi.edu/currentprojects/WHOTS/data/WHOTS-" + \
                       str(roman.toRoman(self.whots_number)) + \
                       "_MET_sys" + str(self.system_number) + ".txt "

        return self.content

    def display_url(self):
        print(self.content)

    def read_whots_sys(self):
        with urlopen(self.content) as download:
            self.read_file = download.read().decode()
        return self.read_file

    def save_whots_sys(self):
        with open("WHOTS-" +
                  str(roman.toRoman(self.whots_number)) +
                  "_MET_sys" + str(self.system_number) +
                  ".txt", 'w') as output:
            output.write(self.read_file)
        return

    def display_text_file(self):
        print("Saving ... " + "WHOTS-" +
              str(roman.toRoman(self.whots_number)) +
              "_MET_sys" + str(self.system_number) + ".txt")


if __name__ == "__main__":
    args = parse_args()
    whots = WhotsFileDownloader(args.whots_number[0], args.system_number[0])
    whots.get_whots_system()
    whots.display_url()
    whots.read_whots_sys()
    whots.save_whots_sys()
    whots.display_text_file()
