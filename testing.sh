#!/bin/bash
exec 3>&1 4>&2
timez=$(TIMEFORMAT="%R"; { time ls 1>&3 2>&4; })
# exec 3>&- 4>&-

echo "$timez"