#!/usr/bin/bash

if [ -z "$1" ] || [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    echo "make_new.sh - create new file templates"
    echo "usage: ./make_new.sh [options] platform_name question_number question_name"
    echo "example: ./make_new.sh Leetcode 1306 jump_game_III"
    echo " "
    echo "options:"
    echo "-h, --help            show brief help"
    echo "-m, --monthly         add monthly leetcode challenge tag"
    exit 0
fi

if [ "$1" == "-m" ] || [ "$1" == "--monthly" ]; then
    monthly=true
    shift
fi

type=$1
number=$2
name=$3

if [ -z "$type" ] || [ -z "$number" ] || [ -z "$name" ]; then
    echo "Missing inputs"
    exit 1
fi

if [ "$type" == "lc" ]; then
    type="Leetcode"
fi

is_monthly () {
    if [ "$monthly" == true ]; then
        echo -e "$(date +%B) Leetcoding challenge\n"
    fi
}

cat > ./algorithms/$name.py << EOL
"""
$type $number
$(is_monthly)
"""


EOL
