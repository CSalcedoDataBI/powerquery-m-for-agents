#!/bin/sh
# The headless profile takes no --patch: its home patch is read from DSH_HOME, which is a
# tmpfs that starts empty, so the privacy patch is copied there on every start.
set -e
mkdir -p "$DSH_HOME/profiles/headless"
cp /cfg/privacy.patch.yml "$DSH_HOME/profiles/headless/cordis.patch.yml"
exec dsh "$@"
