from util.import_util import script_imports

script_imports()

from modules.ui.CaptionUI import CaptionUI
from modules.util.args.CaptionUIArgs import CaptionUIArgs


def main():
    args = CaptionUIArgs.parse_args()

    ui = CaptionUI(None, args.dir, args.include_subdirectories)
    ui.mainloop()


if __name__ == '__main__':
    main()
