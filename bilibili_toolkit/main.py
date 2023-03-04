"""Bilibili Toolkit 哔哩哔哩工具箱
https://github.com/cntvc/Bilibili-Toolkit"""

import argparse

banner = r"""
        \\         //
         \\       //
    #####################     ________   ___   ___        ___   ________   ___   ___        ___
    ##                 ##    |\   __  \ |\  \ |\  \      |\  \ |\   __  \ |\  \ |\  \      |\  \
    ##    //     \\    ##    \ \  \|\ /_\ \  \\ \  \     \ \  \\ \  \|\ /_\ \  \\ \  \     \ \  \
    ##   //       \\   ##     \ \   __  \\ \  \\ \  \     \ \  \\ \   __  \\ \  \\ \  \     \ \  \
    ##                 ##      \ \  \|\  \\ \  \\ \  \____ \ \  \\ \  \|\  \\ \  \\ \  \____ \ \  \
    ##       www       ##       \ \_______\\ \__\\ \_______\\ \__\\ \_______\\ \__\\ \_______\\ \__\
    ##                 ##        \|_______| \|__| \|_______| \|__| \|_______| \|__| \|_______| \|__|
    #####################
        \/         \/                               哔哩哔哩 (゜-゜)つロ 干杯~
"""


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="path to config file")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    print(banner)
