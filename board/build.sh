#!/bin/bash
# Heavily inspired from https://github.com/tarneaux/triboard/blob/main/build.sh
# Usage: ./dev.sh [once]
# Description: Make the PCB file from the keyboard.yaml file.
# Whenever the keyboard.yaml file is modified, the PCB file is regenerated.
# If the "once" argument is passed, the PCB file is only generated once and
# the script exits.

set -e

# Check arguments
if [[ "$1" != "once" && "$1" != "" ]]; then
	echo "Usage: ./dev.sh [once]"
	exit 1
fi

OUTPUT_DIR=board/output

pcbnew_pid=

build() {
	npm run board && \
        {
            if [[ "$pcbnew_pid" ]]; then
                kill "$pcbnew_pid" || true
                rm -rf $OUTPUT_DIR/pcbs/\~sessile.kicad_pcb.lck
            fi
            /Applications/KiCad/KiCad.app/Contents/Applications/pcbnew.app/Contents/MacOS/pcbnew $OUTPUT_DIR/pcbs/sessile.kicad_pcb &
            pcbnew_pid=$!
        } || true
}


build

if [[ "$1" == "once" ]]; then
	exit 0
fi

fswatch board/config.yaml board/footprints/ | (while read; do build; done)
