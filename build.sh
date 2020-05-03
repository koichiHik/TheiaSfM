#!/bin/bash

ROOT_3RD=~/workspace/3rdParty
#CMAKE_BUILD_TYPE=Debug
CMAKE_BUILD_TYPE=Release

cd ..

if [ ! -e ./build ]; then
  mkdir build
fi
cd build

cmake \
  -D CMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE} \
  -D CMAKE_INSTALL_PREFIX="../install" \
  ../TheiaSfM

make -j32

cd ../TheiaSfM
