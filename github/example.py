# example file
import argparse

from cfg_argparser import ConfigArgParser


def parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--file")
    
    return parser

if __name__ == "__main__":
    args = ConfigArgParser(parser(), "config.json", exit_on_change=True).parse_args()
    print(args.file)