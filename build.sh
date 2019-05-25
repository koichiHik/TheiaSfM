#!/bin/bash

ROOT_3RD=~/workspace/3rdParty
#CMAKE_BUILD_TYPE=Debug
CMAKE_BUILD_TYPE=Release
ROCKSDB_HOME=${ROOT_3RD}/rock_sdb/install/

cd ..

if [ ! -e ./build ]; then
  mkdir build
fi
cd build

cmake \
  -D CMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE} \
  -D CMAKE_INSTALL_PREFIX="../install" \
  -D ROCKSDB_HOME=${ROCKSDB_HOME} \
  ../TheiaSfM

make -j32

cd ../TheiaSfM
