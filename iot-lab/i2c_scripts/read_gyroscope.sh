#!/bin/bash
## !/bin/bash -xv ## debug

# https://www.st.com/resource/en/datasheet/lsm9ds1.pdf
lsm9ds1_addr="0x6a"

reading2rad() {
    reading="$1"
    sensitivity_mdps_lsb="8.75"
    echo $(awk "BEGIN { print ($reading * $sensitivity / 1000 / 180) }")
}

deg2rad() {
    # 1st arg = def
    degrees="$1"
    pi="3.14159265358979323846"
    radians=$(awk "BEGIN { print ($degrees * $pi / 180) }")
    echo "$radians"
}

hex2dec() {
    # 1st arg = hex

    echo $(printf "%d" "$1")
}

read_rad() {
    # 1st arg = addr
    
    register_addr="$1"
    hex="$(i2cget -y 1 $lsm9ds1_addr $register_addr w)"
    reading="$(hex2dec $hex)"
    rad="$(reading2rad $reading)"
    echo "$rad" #"$rad"
}

echo "$(read_rad 0x18)"