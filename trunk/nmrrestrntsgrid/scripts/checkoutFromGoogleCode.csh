

set list = ( nmrrestrntsgrid cing wattos )
set x = cing

foreach x ( $list )

cd 
cd sf
rsync -av rsync://$x.cvs.sourceforge.net/cvsroot/$x/$x/\* $x-cvsbackup
cd $x-cvsbackup
cvs2svn -s ../$x-svn .

cd ..
svnsync init --username jurgenfd https://$x.googlecode.com/svn file:///Users/jd/sf/$x-svn

svnsync sync --username jurgenfd https://$x.googlecode.com/svn


# Checking out
set x = nmrrestrntsgrid
cd $WS
if ( $x == 'wattos' ) then
	set root = https://$x.googlecode.com/svn/trunk/
else
    set root = https://$x.googlecode.com/svn/trunk/$x
endif

svn checkout $root $x --username jurgenfd

