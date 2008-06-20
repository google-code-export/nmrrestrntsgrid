"""
This script will start many clones for generating DOCR/FRED entries
in the NMR restraint grid.
"""
from nmrrestrntsgrid.core.PDBEntryLists import getEntryListFromCsvFile
from nmrrestrntsgrid.settings.localConstants import results_dir
from nmrrestrntsgrid.settings.localConstants import scripts_dir
from nmrrestrntsgrid.util import forkoff
from nmrrestrntsgrid.util.jfdutils import Lister
import sys, os, string

class CloneWars( Lister ):

    def __init__(self,
                 verbose                = 2,
                 max_entries_todo       = 1,
                 max_time_to_wait       = 20
                ):

        ## How long to wait between submitting individual jobs when on the cluster.
        self.delay_between_submitting_jobs  = 0
        self.verbose                        = verbose
        self.max_time_to_wait               = max_time_to_wait
        self.script_name                    = 'processDOCR_FRED.csh'
        self.output_dir                     = os.path.join(results_dir, 'perEntry')
        self.entry_list                     = []
        self.max_entries_todo               = max_entries_todo
##No changes required below this line
###############################################################################
        

    """
    Returns 0 for success.
    """
    def do_cmd( self, cmd, entry_code ):
        if self.verbose > 1:
            print "Doing entry", entry_code, cmd

        ##  Try command and check for non-zero exit status
        pipe = os.popen( cmd )
        output = pipe.read()

        ##  The program exit status is available by the following construct
        ##  The status will be the exit number unless the program executed
        ##  succesfully in which case it will be None.
        status = pipe.close()

        if output:
            print output
            
        ## Success    
        if ( status != None ):
            print "ERROR: Failed shell command:"
            print cmd
            print output
            return status #?

    """
    Just making the one page specific for an entry.
    Returns None for success.
    """
    def do_analyses_loop( self, processes_max ):
        ## Setup a job list
    
        job_list = []
        for entry_code in self.entry_list:
            if len(job_list) >= self.max_entries_todo:
                break
            ##  Try command and check for non-zero exit status
            cmd = "%s/%s %s >& %s/%s.log" % (
                  scripts_dir,
                  self.script_name,
                  entry_code,
                  self.output_dir,
                  entry_code )            
            job = ( self.do_cmd, ( cmd, entry_code ) )
            job_list.append( job )

        f = forkoff.ForkOff(
                processes_max       = processes_max,
                max_time_to_wait    = self.max_time_to_wait,
                verbosity           = self.verbose
                )
        self.done_entry_list = f.forkoff_start( job_list, self.delay_between_submitting_jobs )
        if self.verbose == 9:
            print "Finished following list:", self.done_entry_list

    
###############################################################################

        # Use INT signal 2 to signal that this process should stop starting more entries.
        # E.g. kill -s 2 1809
        # Other signals that might be useful
        # HUP  1    TERM 15  
        # INT  2    KILL  9

if __name__ == '__main__':    
    if len(sys.argv) < 3:
        print "ERROR: need to specify the following parameters:"
        print "-1- list filename of entries todo"
        print "-2- number of max processors to use"
        print "-3- number of max entries to do"
        sys.exit(1)
        
    listFileName = sys.argv[1]
    print "Reading entry list from: ", listFileName
    entry_list =  getEntryListFromCsvFile(listFileName)
##    for x in entry_list:
##        if x in PDBEntryLists.listDOCRfREDDone:
##            print "WARNING entry already done: ", x
    if not entry_list:
        print "ERROR: no entries in list todo"
        sys.exit(1)        
##    entry_list.reverse()
    print "Doing %s entries %s\n" % (len(entry_list), entry_list)

    processes_max = string.atoi(sys.argv[2])
    if processes_max < 1 or processes_max > 2:
        print "check parameter for max number of processors to use; expected range: [1-2] but got: ", sys.argv[2]
        sys.exit(1)
        
    max_entries_todo = string.atoi(sys.argv[3])
    if max_entries_todo < 1 or max_entries_todo > 5000:
        print "check parameter for max number of entries to do; expected range: [1-5000] but got: ", sys.argv[3]
        sys.exit(1)

    ## Initialize the project
    c = CloneWars(
        verbose                 = 2,    # 0 gives no output and 9 is all; 2 is default
        max_entries_todo        = max_entries_todo,    # was 500 (could be as many as u like)
        max_time_to_wait        = 6000, # was 1200 (longest one takes only ? seconds)
    )
    c.entry_list = entry_list
    c.do_analyses_loop(processes_max = processes_max) # was 1 
