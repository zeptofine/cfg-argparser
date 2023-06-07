import multiprocessing
from enum import Enum
from pathlib import Path
from typing import Literal, Optional

import typer
from rich import print as rprint
from typing_extensions import Annotated

from cfg_argparser import CfgDict, wrap_config

CPU_COUNT = int(multiprocessing.cpu_count())
app = typer.Typer()


class LimitModes(str, Enum):
    """Modes to limit the output images based on a timestamp."""

    BEFORE = "before"
    AFTER = "after"


class HashModes(str, Enum):
    """Modes to hash the images to compare."""

    AVERAGE = "average"
    CROP_RESISTANT = "crop_resistant"
    COLOR = "color"
    DHASH = "dhash"
    DHASH_VERTICAL = "dhash_vertical"
    PHASH = "phash"
    PHASH_SIMPLE = "phash_simple"
    WHASH = "whash"


class HashChoices(str, Enum):
    """How to decide which image to keep / remove."""

    IGNORE_ALL = "ignore_all"
    NEWEST = "newest"
    OLDEST = "oldest"
    SIZE = "size"


dct = CfgDict("test.json")


@app.command()
@wrap_config(cfg_dict=dct)
def run(
    input_folder: Annotated[Path, typer.Option(help="Input folder.")],
    scale: Annotated[int, typer.Option(help="the scale to downscale.")] = 4,
    extension: Annotated[Optional[str], typer.Option(help="export extension.")] = None,
    recursive: Annotated[bool, typer.Option(help="preserves the tree hierarchy.")] = False,
    threads: Annotated[int, typer.Option(help="number of threads for multiprocessing.")] = int(CPU_COUNT * (3 / 4)),
    limit: Annotated[Optional[int], typer.Option(help="only gathers a given number of images.")] = None,
    limit_mode: Annotated[LimitModes, typer.Option(help="which order the limiter is activated.")] = LimitModes.BEFORE,
    simulate: Annotated[bool, typer.Option(help="skips the conversion step. Used for debugging.")] = False,
    purge: Annotated[bool, typer.Option(help="deletes the output files corresponding to the input files.")] = False,
    purge_all: Annotated[bool, typer.Option(help="Same as above, but deletes *everything*.")] = False,
    overwrite: Annotated[bool, typer.Option(help="Skips checking existing files, overwrites existing files.")] = False,
    whitelist: Annotated[Optional[str], typer.Option(help="only allows paths with the given strings.")] = None,
    blacklist: Annotated[Optional[str], typer.Option(help="Excludes paths with the given strings.")] = None,
    list_separator: Annotated[Optional[str], typer.Option(help="separator for the white/blacklists.")] = None,
    minsize: Annotated[
        Optional[int], typer.Option(help="minimum size an image must be.", rich_help_panel="sizing")
    ] = None,
    maxsize: Annotated[Optional[int], typer.Option(help="maximum size an image can be.")] = None,
    crop_mod: Annotated[bool, typer.Option(help="changes mod mode to crop the image to be divisible by scale")] = False,
    before: Annotated[Optional[str], typer.Option(help="only uses files before a given date")] = None,
    after: Annotated[Optional[str], typer.Option(help="only uses after a given date.")] = None,
    # ^^ these will be parsed with dateutil.parser ^^
    hash_images: Annotated[bool, typer.Option(help="Removes perceptually similar images.")] = False,
    hash_mode: Annotated[
        HashModes,
        typer.Option(help="How to hash the images. read https://github.com/JohannesBuchner/imagehash for more info"),
    ] = HashModes.AVERAGE,
    hash_choice: Annotated[
        HashChoices, typer.Option(help="What to do in the occurance of a hash conflict.")
    ] = HashChoices.IGNORE_ALL,
) -> int:
    rprint(
        input_folder,
        scale,
        extension,
        recursive,
        threads,
        limit,
        limit_mode,
        simulate,
        purge,
        purge_all,
        overwrite,
        whitelist,
        blacklist,
        list_separator,
        minsize,
        maxsize,
        crop_mod,
        before,
        after,
        hash_images,
        hash_mode,
        hash_choice,
    )
    print(f"Hello {input_folder}")
    return 0


if __name__ == "__main__":
    app()
