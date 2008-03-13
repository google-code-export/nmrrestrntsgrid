"""
Usefull for starting multiple independent processes given a function and list
of arguments when the process might hang or crash and leave zombies around.
Convenient clean up provided. See test code for examples. Only runs on systems
supporting os.fork() call; Unix.

Verbosity of output can be set for the two classes with the following meaning
# 0 Only errors,
# 1 and warnings,
# 2 and other stuff, this is the normal output level!
# 9 All the above and some debug info.

Author: Jurgen F. Doreleijers, BMRB, September 2001
"""

__author__    = "$Author$"
___revision__ = "$Revision$"
___date__     = "$Date$"

"""
$Log$
Revision 1.1  2008/03/13 15:13:03  jurgenfd
Created a layout for python code. Moving code out of the recoord project.

Revision 1.1  2006/06/07 19:33:51  jurgen_bmrb.wisc.edu
JFD Added files for running on multiple processors with automatic time limits and process kills
and guessing the offset between restraint and seqres numbering.

Revision 1.2  2005/06/03 15:14:13  jurgen
*** empty log message ***

Revision 1.1.1.1  2003/03/17 17:22:10  jurgen


Revision 1.1.1.1  2001/10/03 16:13:48  jurgen
Non-working version but good to start with

"""


import sys
import os
import time, types, signal

class ForkOff:

    def __init__( self,
            ## Number of processes that will be spawned/forked off. This could
            ## usually be set to the number of processors
            processes_max               = 1,
            ## Time in seconds a single function may take to complete execution
            ## and return.
            max_time_to_wait            = 60,
            ## After a killing signal how long do we wait for it to die, and
            ## perhaps try killing it again.
            max_time_to_wait_kill       = 5,
            ## Time to wait in parent by sleeping if no process finished
            time_to_wait                = 1,
            ## Verbosity of output
            verbosity                   = 2
            ):
        
        ## Parallel processing options:
        ## Maximum number of simultanuous subprocesses
        self.processes_max          = processes_max
        ## Currently open subprocesses
        self.processes_open         = 0
        ## Total number of started subprocesses
        self.processes_started      = 0
        ## Total number of finished subprocesses
        self.processes_finished     = 0
        ## Total number of subprocesses to be done if all scheduled to be done
        ## are indeed to be done. This is set later on and perhaps adjusted
        ## when the user interrupts the process by ctrl-c.
        self.processes_todo         = 0
        ## List of jobs fids that were done correctly (jobs are numbered as in
        ## array (0..n-1)
        self.done_jobs_list         = []
        ## Dictionary with pid:fid info on running subprocesses
        ## fid is forkoff id.
        self.process_d              = {}
        ## Dictionary with pid:seconds info on running subprocesses
        self.process_t              = {}
        ## Maximume number of seconds to wait for a subprocesses
        self.max_time_to_wait       = max_time_to_wait
        ## See above
        self.time_to_wait           = time_to_wait
        ## See above
        self.verbosity              = verbosity
        ## Use methods provided by Process class
        ## Maximume number of seconds to wait after killing a subprocesses
        self.max_time_to_wait_kill  = max_time_to_wait_kill

        ## Initialize an instance of the Process class
        self.p                      = Process(
            max_time_to_wait_kill   = self.max_time_to_wait_kill,
            verbosity               = self.verbosity
            )

    """
    Main loop
    job_list should be of a list of tuples. The tuple should contain
    a function and a tuple with one or more arguments.
    E.g. [( my_sleep, (990.1,) ), ( my_sleep, (990.1,) )]
    Returns a list of ids of processes (id is the index of the job in the list
    of jobs) that were done AND done successfully.
    Empty lists will be returned if nothing gets done successfully
    """
    def forkoff_start( self, job_list, delay_between_submitting_jobs ):
        
        ## Check job list for variable type errors
        for job in job_list:
            func = job[0]
            args = job[1]
            if type(args) != types.TupleType:
                print "ERROR: given argument not of type Tuple for job: ", job
                return []
            if not ( type(func) == types.FunctionType or
                     type(func) == types.BuiltinFunctionType or
                     type(func) == types.MethodType ) :
                print "ERROR: given function not of types:"
                print "(Function, BuiltinFunctionType, or MethodType) for job:"
                print job
                print "In stead type is : ", type(func)
                return []
                
        ## Maximum number of processes to do
        self.processes_todo = len( job_list )
        if self.processes_todo == 0:
            if self.verbosity:
                print "WARNING: No new processes to do so none to start"
            return []
            
        if self.verbosity > 1:
            print "Doing %s new processes" % self.processes_todo

        ## Keep making pages until an uncatched Exception occurs
        ## That would be a ctrl-c or so. The ctrl-c is also caught by
        ## subprocesses within python at least.
        ## I have not found a way to use this mechanism for jobs
        ## running in the background of a now killed terminal.
        ## When I read up, I got indications that the signal handlers
        ## for INTerrupt and QUIT might be rerouted and not available
        ## anymore. A hard kill is then needed.
        ##
        try:
            self.do_jobs( job_list, delay_between_submitting_jobs )
        except KeyboardInterrupt:
            if self.verbosity:
                print "WARNING: Caught interrupt in parent."
                print "WARNING: Trying to finish up by waiting for subprocesses"

        ## Finish waiting for subprocesses
        ## Don't make any new!
        self.processes_todo = self.processes_started
        try:
            self.do_jobs( job_list, delay_between_submitting_jobs )
        except KeyboardInterrupt:
            if self.verbosity:
                print "WARNING: Again caught interrupt in parent."
                print "WARNING: Can't finish if you don't let me."
            raise KeyboardInterrupt
            
        ## Any subprocesses left
        if self.process_d:
            key_list = self.process_d.keys()
            key_list.sort()
            for pid in key_list:
                print "ERROR: subprocesses with fid [%s] was left behind with pid [%d]" \
                      % ( self.process_d[ pid ], pid )

        ## Check all were done
        if self.processes_finished != len( job_list ):
            if self.verbosity > 1:
                print "WARNING: only %s out of %s jobs were started (not all succesfully finished perhaps)" \
                      % ( self.processes_finished, len( job_list ) )

        ## Check if all finished correctly
        if self.processes_finished != self.processes_started:
            str = "ERROR: Number of processes finished and started do not match"
            str += `self.processes_finished` + " " + `self.processes_started`
            raise str

        if self.verbosity > 1:
            print "Finished %s out of the %s processes successfully" \
                  % ( len( self.done_jobs_list), self.processes_todo )

        ## List of job numbers that were done.
        return self.done_jobs_list


    """
    Starting independent processes given a list of function with
    list of arguments
    """
    def do_jobs( self, job_list, delay_between_submitting_jobs ):

        while ( self.processes_started  < self.processes_todo or
                self.processes_open     > 0 ):
            sys.stdout.flush()
            sys.stderr.flush()
            ## Start new or wait for old process
            if ( self.processes_open    < self.processes_max  and
                 self.processes_started < self.processes_todo ):
                func = job_list[ self.processes_started ][0]
                args = job_list[ self.processes_started ][1]
                self.processes_open     += 1
                self.processes_started  += 1
                pid = self.p.process_fork( func, args )
                ## Push pid/fid onto dictionary of things running
                self.process_d[ pid ] = self.processes_started - 1
                self.process_t[ pid ] = time.time()
                time.sleep(delay_between_submitting_jobs)
            elif self.processes_open:
                keys = self.process_d.keys()
                for pid in keys:
                    exit_pid, exit_status = self.p.process_wait( pid, os.WNOHANG )
                    if exit_pid:
                        if self.verbosity > 3:
                            print "DEBUG: Process with pid [%s] exited with status [%s]" % \
                              (exit_pid, exit_status)
                        ## Pop pid/args from dictionary
                        fid = self.process_d[ exit_pid ]
                        del self.process_d[ exit_pid ]
                        del self.process_t[ exit_pid ]
                        self.processes_open     -= 1
                        self.processes_finished += 1
                        ## Only consider things done if done correctly
                        if exit_status:
                            if self.verbosity:
                                print "WARNING: Process with fid: [%s] considered NOT done" % fid
                        else:
                            if self.verbosity > 3:
                                print "DEBUG: Process with fid: [%s] considered done" % fid
                            self.done_jobs_list.append( fid )
                ## Give the cpu 1 second rest in between the checks
                ## if no process has exited
                time.sleep ( self.time_to_wait )

            ## Check to see if time's done for any
            keys = self.process_t.keys()
            for pid in (keys):
                if ( time.time() - self.process_t[ pid ] >
                     self.max_time_to_wait ):
                    ## Pop pid/args from dictionary
                    fid = self.process_d[ pid ]
                    del self.process_d[ pid ]
                    del self.process_t[ pid ]
                    self.processes_open     -= 1
                    self.processes_finished += 1
                    if self.verbosity:
                        print "WARNING: Process with fid [%s] was not done within time limits" \
                              % fid
                        print "WARNING: Process is not considered done"
                    _exit_pid, _exit_status = self.p.process_kill( pid )
                    ## If a process needed to be killed then
                    ## don't check for others in this iteration.
                    ## This is to prevent processes being killed that might
                    ## already be finished but didn't get a chance to be reaped
                    ## because the process_kill takes quite some time.
                    break




"""
Class for process oriented functions used by ForkOff.
"""
class Process:

    def __init__( self,
            ## After sending a killing signal how long do we wait for it to die (and perhaps
            ## try killing it again.
            max_time_to_wait_kill       = 5,
            ## Time to wait in parent by sleeping if no process finished
            verbosity                   = 2
            ):

        ## Maximume number of seconds to wait after killing a subprocesses
        self.max_time_to_wait_kill  = max_time_to_wait_kill

        ## See ForkOff class
        self.verbosity              = verbosity

        ## Number for the exit status as returned by pipe.close() normally
        ## corresponding to exit status 1
        self.exit_status_failure    = 256


    def process_fork( self, function, arguments ):

        pid = os.fork()

        if pid:
            ## Parent here
            if self.verbosity > 3:
                print "Forked an independent process with pid: ", pid
            return pid

        if pid == None:
            print "ERROR: pid is None after fork, unknown error to coder"
            print "ERROR: child returns"
            return pid

        ## Subprocess here
        ## Define exit status is an error for child if not changed
        exit_status = 1

        if pid != 0:
            str = "ERROR: code error in Fork, process_start, pid =" + `os.getpid()`
            raise str
        if self.verbosity > 2:
            print "DEBUG: Starting subprocess with pid:", os.getpid()
        if self.verbosity > 8:
            print "DEBUG: Setting gpid from [%s] to current pid" % os.getpgrp()

        os.setpgid(0,0)
        if self.verbosity > 8:
            print "DEBUG: After setgpid: Current gpid: [%s], pid: [%s]" % ( os.getpgrp(), os.getpid() )

        try:
            exit_status = apply( function, arguments )
        except KeyboardInterrupt:
            if self.verbosity:
                print "WARNING: Caught KeyboardInterrupt in subprocess, subprocess will exit(1)"
            os._exit(1)
##        except:
##            print "ERROR: Caught exception other than KeyboardInterrupt, subprocess will exit(1)"
##            os._exit(1)

        if exit_status:
            if self.verbosity > 1:
                print "Subprocess will do error exit with exit code 1"
            os._exit(1)
        else:
            if self.verbosity > 2:
                print "DEBUG: Subprocess will do normal exit with exit code 0"
            os._exit(0)



    def process_wait( self, pid=0, options=0 ):
        if self.verbosity > 8:
            print "DEBUG: Wait for process: [%s] with options: [%s] " % ( pid, options )

        ## Indicating failure
        exit_pid, exit_status = 0, self.exit_status_failure

        if os.getpid() == pid:
            if self.verbosity:
                print "WARNING: given pid is for current process, giving up"
            return exit_pid, exit_status

        try:
            exit_pid, exit_status = os.waitpid(pid, options)
        except OSError, info:
            if self.verbosity:
                print "WARNING: caught an OSError with info:", info

        return exit_pid, exit_status


    def process_signal( self, pid, sig ):
        if self.verbosity > 1:
            print "Signal process: [%s] with signal [%s]" % ( pid, sig )
        if os.getpid() == pid:
            if self.verbosity:
                print "WARNING: given pid is for current process, giving up"
            return 1
        
        try:
            os.kill( pid, sig )
        except OSError, info:
            if self.verbosity:
                print "WARNING: caught an OSError with info:", info
            return 0


    def process_kill( self, pid ):
        if self.verbosity > 1:
            print "Signaling process: [%s] for a kill" % pid
        if os.getpid() == pid:
            if self.verbosity:
                print "WARNING: given pid is for current process, giving up"
            return 0, self.exit_status_failure

        if self.verbosity > 2:
            print "Process and subprocesses will be signaled by a TERM signal"
        ## On my linux box urchin:
        ## HUP  1    TERM 15  
        ## INT  2    KILL  9
        ## Please not the minus sign in front of the pid which tells kill to
        ## kill all processes with that pid for its **group process id**
        ## Took 2 days to figure out...
        self.process_signal( -pid, signal.SIGTERM )
        if self.verbosity > 2:
            print "Sleeping ", self.max_time_to_wait_kill
        time.sleep(self.max_time_to_wait_kill)
        exit_pid, exit_status = self.process_wait( pid, os.WNOHANG )
        if exit_pid:
            if self.verbosity > 1:
                print "Process with pid [%s] was killed by TERM signal" % exit_pid
        else:
            if self.verbosity > 2:
                print "Process was not killed, now it will be signaled a KILL signal"
            self.process_signal( -pid, signal.SIGKILL )
            if self.verbosity > 2:
                print "DEBUG: Sleeping ", self.max_time_to_wait_kill
            time.sleep(self.max_time_to_wait_kill)
            exit_pid, exit_status = self.process_wait( pid, os.WNOHANG )
            if exit_pid > 1:
                print "Process with pid [%s] was killed by KILL signal" % exit_pid
            else:
                print "ERROR:   Process could NOT be killed by HUP or KILL signal"
                print "ERROR:   Process has turned into zombie"
        if self.verbosity >= 9:
            print "Got exit_pid, exit_status:", exit_pid, exit_status
        
        return exit_pid, exit_status


###############################################################################

# Test code.
            
def my_sleep( arg ):

    ## Check types
    if type(arg) == types.TupleType:
        print "ERROR: Type of args [%s] is tuple" % arg
        print "ERROR: This can happen when supplied with more than 1 argument"
        return 1

    ## Take first argument
    print "Sleeping for ", arg
    time.sleep ( arg )
    print "Going back to caller"
    return 0

if __name__ == '__main__':

    ## Initializing f will also initialize an instance of class Process
    f = ForkOff(
            processes_max       = 3,
            max_time_to_wait    = 10,
            verbosity           = 2
            )

    ## Sleep long
    job_0       = ( my_sleep, (9999,) )
    ## Sleep
    job_1       = ( my_sleep, (5.1,) )
    ## Sleep short
    job_2       = ( my_sleep, (1.2,) )
    job_list    = [ job_0, job_1, job_2 ]

    done_list   = f.forkoff_start( job_list, 0 )    
    print "Finished ids:", done_list
        
