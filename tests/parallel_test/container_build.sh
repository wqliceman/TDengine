#!/bin/bash

function usage() {
    echo "$0"
    echo -e "\t -w work dir"
    echo -e "\t -e enterprise edition"
    echo -e "\t -t make thread count"
    echo -e "\t -h help"
}

ent=0
while getopts "w:t:eh" opt; do
    case $opt in
        w)
            WORKDIR=$OPTARG
            ;;
        e)
            ent=1
            ;;
        t)
            THREAD_COUNT=$OPTARG
            ;;
        h)
            usage
            exit 0
            ;;
        \?)
            echo "Invalid option: -$OPTARG"
            usage
            exit 0
            ;;
    esac
done

if [ -z "$WORKDIR" ]; then
    usage
    exit 1
fi
if [ -z "$THREAD_COUNT" ]; then
    THREAD_COUNT=1
fi

ulimit -c unlimited

if [ $ent -eq 0 ]; then
    REP_DIR=/home/TDengine
    REP_REAL_PATH=$WORKDIR/TDengine
    REP_MOUNT_PARAM=$REP_REAL_PATH:/home/TDengine
else
    REP_DIR=/home/TDinternal
    REP_REAL_PATH=$WORKDIR/TDinternal
    REP_MOUNT_PARAM=$REP_REAL_PATH:/home/TDinternal
fi
date 
docker run \
    -v $REP_MOUNT_PARAM \
    --rm --ulimit core=-1 taos_test:v1.0 sh -c "cd $REP_DIR;rm -rf debug;mkdir -p debug;cd debug;cmake .. -DBUILD_HTTP=false -DBUILD_TOOLS=true -DBUILD_TEST=true -DWEBSOCKET=true;make -j $THREAD_COUNT || exit 1"

if [[ -d ${WORKDIR}/debugNoSan  ]] ;then
    echo "delete  ${WORKDIR}/debugNoSan"
    rm -rf  ${WORKDIR}/debugNoSan
fi
if [[ -d ${WORKDIR}/debugSan ]] ;then
    echo "delete  ${WORKDIR}/debugSan"
    rm -rf  ${WORKDIR}/debugSan
fi

mv  ${REP_REAL_PATH}/debug  ${WORKDIR}/debugNoSan
date
docker run \
    -v $REP_MOUNT_PARAM \
    --rm --ulimit core=-1 taos_test:v1.0 sh -c "cd $REP_DIR;rm -rf debug;mkdir -p debug;cd debug;cmake .. -DBUILD_HTTP=false -DBUILD_TOOLS=true -DBUILD_TEST=true -DWEBSOCKET=true  -DSANITIZER=true;make -j $THREAD_COUNT || exit  "

mv  ${REP_REAL_PATH}/debug  ${WORKDIR}/debugSan

ret=$?
exit $ret

