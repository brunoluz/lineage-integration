#!/bin/bash

if [ ! -d "marquez" ]; then
  git clone https://github.com/MarquezProject/marquez.git
fi

cd marquez/docker
./up.sh