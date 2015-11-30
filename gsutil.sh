#!/bin/sh
# Install  gsutil, https://storage.googleapis.com/pub/gsutil.tar.gz
# You can either add this here, or configure them on the environment tab of your
# project settings.
GSUTIL_VERSION="4.16"
GSUTIL_DIR=${GSUTIL_DIR:="$HOME/gsutil"}
set -e
CACHED_DOWNLOAD="${HOME}/cache/gsutil.tar.gz"
mkdir -p "${GSUTIL_DIR}"
wget --continue --output-document "${CACHED_DOWNLOAD}" "https://storage.googleapis.com/pub/gsutil.tar.gz"
tar -xaf "${CACHED_DOWNLOAD}" --strip-components=1 --directory "${GSUTIL_DIR}"
ln -s "${GSUTIL_DIR}/gsutil" "${HOME}/bin/gsutil"
# check that everything worked
gsutil version
