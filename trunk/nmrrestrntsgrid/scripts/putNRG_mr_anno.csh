#!/bin/csh -f
# Author: Jurgen F. Doreleijers
# $CINGROOT/scripts/cing/putNRG_mr_anno.csh

set SERVER=jurgend@www.cmbi.ru.nl
set CLIENT=jd@nmr.cmbi.umcn.nl
# trailing slash is important.
set SOURCEDIR=/grunt/raid/backup/mr_anno_backup/
# your top level rsync directory needs to exist
set MIRRORDIR=/Users/jd/wattosTestingPlatform/Wattos/mr_anno_backup

###################################################################

## No changes below except user id and specific word such as azvv.

# leaving out options of verbosity so I get a smaller email.
rsync -a -f '+ */1brv.mr' -f '- */*' \
    --delete --stats \
    --bwlimit 80 \
    --progress -v \
    -e "ssh $SERVER ssh" \
    $SOURCEDIR $CLIENT':'$MIRRORDIR

echo "Finished"