

find $big_dir -name "*.str" | xargs gzip

find $ccpn_tmp_dir/data/recoord/1brv -name linkNmrStarData -ok rm -rf {} \;