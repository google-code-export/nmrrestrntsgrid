topology 
    @TOPPAR:nucleic.top
    @TOPPAR:protein.top
    @TOPPAR:ion.top
end

parameter 
    @TOPPAR:nucleic.par
    @TOPPAR:protein.par
    @TOPPAR:ion.par
end
    

structure @1xxx.psf end
coor @1xxx_extended.pdb 

! inspect the ade amide
constraint interaction
(resn asp )
(resn asp )
end

(name h#1))
(resn ade or resn cyt or resn gua or res)

! inspect the phosphate topology
constraint interaction
((name p or name o5' or name o3' or name op#))
((name p or name o5' or name o3' or name op#))
end

print thres=0 impr


print thres=0 bonds
print thres=0 angle
print thres=0 dihe

