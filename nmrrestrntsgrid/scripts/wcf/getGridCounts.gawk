{
    if (NR==1) {
        p=$(NF) 
        if ( p == "full" ) { 
             print x,"No items counted" 
             exit 
        } 
    } 
    if (NR==2) {
        c=$(NF) 
        per = 0 
        if (p > 0 ) {
            per = 100.0*c/p
        }
        if (per<cutoff) {
            printf ("%4s Counts %5d %5d %5.1f\n", x,p,c,per)
        }
    }
}