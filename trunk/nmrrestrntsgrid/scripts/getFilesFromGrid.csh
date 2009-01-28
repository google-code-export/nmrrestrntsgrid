#!/bin/csh -f 
# Author: Jurgen F. Doreleijers 
# Wed Dec 14 13:49:06 CST 2005
#
# TASK: Gets the files needed for 3rd stage out of NRG. 
# USE:  $scripts_dir/getFilesFromGrid.csh 1a4d,1brv

set run_id          = all
set par1            = "block_text_type=2-parsed&file_detail=2-parsed&format=n%2Fa"
#set par2            = "request_type=archive&subtype=full&type=entry&db_username=wattos2"
set par2            = "request_type=archive&subtype=full&type=entry"
set par3            = "pdb_id=1brv,1hue"

# Get argument pdb codes (comma seperated if it exists.)
if ( $1 != "" ) then
    set par3 = "pdb_id=$1"
    ##echo "Using pdb ids: $1"
endif

# Uncomment if you want to get all files
#set par3            = ""
set zipFile         = $run_id.zip
set wgetLogFile     = $run_id"_wget".log
set unzipLogFile    = $run_id"_unzip".log
set scriptFile      = $run_id.csh

## No changes below next line
########################################################################
echo "Using pdb ids [all if none given]: $par3"
if ( -e $dir_restraint/$run_id ) then
    \rm -rf $dir_restraint/$run_id
endif
mkdir $dir_restraint/$run_id
cd $dir_restraint/$run_id

echo "-1- Getting files from NMR Restraint Grid"
# Write all output to 1 zip file as it should be.
\rm -f $zipFile >& /dev/null
wget -v -o $wgetLogFile -O $zipFile $servletUrl'?'"$par1&$par2&$par3"
if ( $status ) then
    echo "ERROR: failed to wget from url: $servletUrl"
    exit 1
endif
if ( ! -e $zipFile ) then
    echo "ERROR: failed to find zip file: $zipFile"
    exit 1
endif


echo "-2- Unzipping"
unzip $zipFile > $unzipLogFile
echo "-3- Getting info from index file."
gawk -F',' '{if ((NR==1)||(NF<14))next;printf "mv block_%s.str %s_rst.str\n",$2,$3}' index.csv > $scriptFile
    
chmod +x $scriptFile
echo "-4- Renaming all files."
$scriptFile
if ( $status ) then
    echo "ERROR: failed scriptFile: $scriptFile"
    exit 1
endif
echo "-5- Moving files to standard dir."
\mv -f *_rst.str $dir_restr_unzip
if ( $status ) then
    echo "ERROR: failed mv"
    exit 1
endif
