#!/bin/sh
#
#
# @Author: @korutx
# @Date:   2020-07-22 14:05:43
# @Usage: ./run.sh runserver

SCRIPT=`realpath -s $0`
ROOTDIR=`dirname "$SCRIPT"`

PYTHON=$(source "$ROOTDIR/bin/check-python.sh")

if [[ "$PYTHON_REF" == "NoPython" ]]; then
    echo "Python3.6+ is not installed."
    exit 1
fi


runserver() {
    if test -f "$ROOTDIR/src/certberus/local/settings.py"; then
        export DJANGO_SETTINGS_MODULE="local.settings"
    fi
    cd "$ROOTDIR/src/certberus" && python manage.py runserver $@ 
}

init() {
    FILE="$ROOTDIR/venv3/bin/activate"
    if ! test -f "$FILE"; then
        $PYTHON -m virtualenv "$ROOTDIR/venv3"
        pip install -r "$ROOTDIR/requirements.txt"
    fi
    echo "Initialization is ready! Please activate executing: . $FILE"
}

if [ "x$1" = "xrunserver" ]; then
    shift
    runserver $@
elif [ "x$1" = "xinit" ]; then
    shift
    init $@
# elif [ "x$1" = "xstop" ]; then
#     stop_tomcat
#     sleep 2
# elif [ "x$1" = "xstatus" ]; then
#     is_tomcat_running
#     echo $TOMCAT_STATUS
# elif [ "x$1" = "xcleanpid" ]; then
#     cleanpid
fi
