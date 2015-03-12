# do only once #
```
cd /big/docr
cvs -d :pserver:anonymous@ccpforge.cse.rl.ac.uk:/cvsroot/ccpn-chemcomp checkout ccpn-chemcomp # will take a few mintues.
cd $CCPNMR_TOP_DIR
ln -s /big/docr/ccpn-chemcomp .
```

# update #
```
cd $CCPNMR_TOP_DIR/ccpn-chemcomp # might lead you to follow the symbolic link.
cvs update .
```

# access from code #
```
ls $CCPNMR_TOP_DIR/ccpn-chemcomp 
```

This will display a directory of all the symbolic links to the actual data.